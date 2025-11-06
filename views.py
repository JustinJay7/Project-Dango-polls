from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from .forms import CustomUserCreationForm, LoginForm
import logging
from datetime import datetime

logger = logging.getLogger(__name__)
# Polls views
def index(request):
    logger.info(f"Accessed index at {datetime.now()}")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def home(request):
    return render(request, 'polls/index.html')

def detail(request, question_id):
    logger.info(f"Accessed detail for question {question_id} at {datetime.now()}")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    logger.info(f"Accessed results for question {question_id} at {datetime.now()}")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
   
@login_required
def vote(request, question_id):
    logger.info(f"User {request.user.username} attempted to vote at {datetime.now()}")
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# Authentication views
def register(request):
    logger.info(f"Accessed register page at {datetime.now()}")
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            logger.info(f"New user registered: {user.username} at {datetime.now()}")
            return redirect('polls:index')
        else:
            logger.warning(f"Registration failed at {datetime.now()}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})

def user_login(request):
    logger.info(f"Accessed login page at {datetime.now()}")
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                logger.info(f"User {username} logged in at {datetime.now()}")
                return redirect('polls:index')
            else:
                messages.error(request, "Invalid username or password.")
                logger.warning(f"Failed login attempt for {username} at {datetime.now()}")
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})

@login_required
def user_logout(request):
    logger.info(f"User {request.user.username} logged out at {datetime.now()}")
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('polls:index')

@login_required
def profile(request):
    return render(request, 'polls/templates/authentication/profile.html')
