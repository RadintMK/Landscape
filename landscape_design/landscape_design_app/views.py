from .models import PortfolioProject, BlogPost, Service
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')

def services(request):
    services = Service.objects.filter(is_active=True)
    return render(request, 'services.html', {'services': services})

def portfolio(request):
    projects = PortfolioProject.objects.all() 
    return render(request, 'portfolio.html', {'projects': projects})

def blog(request):
    posts = BlogPost.objects.all().order_by('-created_at')  # Получаем все посты, отсортированные по дате
    return render(request, 'blog.html', {'posts': posts})


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = form.cleaned_data['subject']

            # Отправляем сообщение на email
            send_mail(
                f'Новое сообщение от {name} - {subject}',
                message,
                email,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            # Отображаем сообщение об успешной отправке
            return render(request, 'contacts.html', {'message_sent': True})

    else:
        form = ContactForm()

    return render(request, 'contacts.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error'})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error'})

def logout_view(request):
    logout(request)
    return redirect('index')