from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Announcement
from members .models import Member

# Create your views here.
def index(request):
    announcements = Announcement.objects.order_by('-date').filter(is_published=True)
    context= {
        'announcements': announcements
    }
    return render(request, 'pages/index.html' , context)

def about(request):
    return render(request, 'pages/about.html', {})

def services(request):
    return render(request, 'pages/services.html', {})

def community(request):
    return render(request, 'pages/community.html', {})

def education(request):
    return render(request, 'pages/education.html', {})

@login_required(login_url='/authenticate/login/')
def members(request):
    members= Member.objects.all()
    context = {
        'members': members
    }
    return render(request, 'pages/members.html', context)
