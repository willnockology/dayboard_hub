from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Company, Yacht, Category, Form, FormField, Comment, Notification, User
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is the index page.")

@login_required
def dashboard(request):
    # Logic for dashboard view
    context = {}
    return render(request, 'yacht_app/dashboard.html', context)

@login_required
def yacht_detail(request, yacht_id):
    yacht = get_object_or_404(Yacht, id=yacht_id)
    context = {'yacht': yacht}
    return render(request, 'yacht_app/yacht_detail.html', context)

@login_required
def form_detail(request, form_id):
    form = get_object_or_404(Form, id=form_id)
    context = {'form': form}
    return render(request, 'yacht_app/form_detail.html', context)

@login_required
def comment_detail(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    context = {'comment': comment}
    return render(request, 'yacht_app/comment_detail.html', context)

@login_required
def notification_detail(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    context = {'notification': notification}
    return render(request, 'yacht_app/notification_detail.html', context)

# Other views and functions can be defined here as required
