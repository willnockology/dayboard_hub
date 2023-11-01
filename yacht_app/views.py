from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from .models import Company, Yacht, Category, Form, FormField, Comment, Notification, User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    # Logic for dashboard view
    context = {}
    return render(request, 'dashboard.html', context)

@login_required
def yacht_detail(request, yacht_id):
    yacht = get_object_or_404(Yacht, id=yacht_id)
    context = {'yacht': yacht}
    return render(request, 'yacht_detail.html', context)

@login_required
def form_detail(request, form_id):
    form = get_object_or_404(Form, id=form_id)
    context = {'form': form}
    return render(request, 'form_detail.html', context)

@login_required
def comment_detail(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    context = {'comment': comment}
    return render(request, 'comment_detail.html', context)

@login_required
def notification_detail(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    context = {'notification': notification}
    return render(request, 'notification_detail.html', context)

@login_required
def profile(request):
    return render(request, 'profile.html')

def user_create_or_update(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = None

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('some_view')
    else:
        form = UserForm(instance=user)

    context = {
        'form': form,
    }
    return render(request, 'path_to_template.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def your_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the home page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'index.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'index.html')
    
    # yacht_app/views.py

def home(request):
    return render(request, 'home.html')

class UserLoginView(LoginView):
    template_name = 'login.html'
    
class UserLogoutView(LogoutView):
    template_name = 'logout.html'  
    
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})





