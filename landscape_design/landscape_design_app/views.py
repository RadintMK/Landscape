# landscape_design_app/views.py

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.db.models import Q, Count
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    Contact, PortfolioProject, BlogPost, Service, ServiceCategory,
    BlogCategory, PortfolioCategory, BlogTag,
)
from .forms import ContactForm
import re

def _parse_list_from_text(text_data):
    if not text_data:
        return []
    items = [item.strip() for item in re.split(r'[,\n]+', text_data) if item.strip()]
    return items

def index(request):
    contacts = Contact.objects.first()
    parsed_contacts = {}
    if contacts:
        parsed_contacts['address'] = contacts.address
        parsed_contacts['phone_numbers'] = _parse_list_from_text(contacts.phone_numbers)
        parsed_contacts['emails'] = _parse_list_from_text(contacts.emails)
        parsed_contacts['work_hours'] = contacts.work_hours
        parsed_contacts['weekend_hours'] = contacts.weekend_hours
        parsed_contacts['map_url'] = contacts.map_url
        parsed_contacts['social_media'] = contacts.social_media

    services = Service.objects.filter(is_active=True)
    portfolio = PortfolioProject.objects.all()[:3]
    blog_posts = BlogPost.objects.order_by('-created_at')[:3]

    return render(request, 'index.html', {
        'contacts': parsed_contacts,
        'services': services,
        'portfolio': portfolio,
        'blog_posts': blog_posts,
    })

def services(request):
    services_list = Service.objects.filter(is_active=True)
    categories = ServiceCategory.objects.all()
    return render(request, 'services.html', {'services': services_list, 'categories': categories})

def portfolio(request):
    projects = PortfolioProject.objects.all()
    categories = PortfolioCategory.objects.all()
    return render(request, 'portfolio.html', {'portfolio': projects, 'portfolio_categories': categories})

def blog(request):
    posts_list = BlogPost.objects.filter(is_published=True).select_related('author', 'category').prefetch_related('tags')

    selected_category_slug = request.GET.get('category')
    selected_tag_slug = request.GET.get('tag')
    search_query = request.GET.get('q')

    if selected_category_slug:
        posts_list = posts_list.filter(category__slug=selected_category_slug)

    if selected_tag_slug:
        posts_list = posts_list.filter(tags__slug=selected_tag_slug)

    if search_query:
        posts_list = posts_list.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(preview__icontains=search_query)
        ).distinct()

    paginator = Paginator(posts_list, 6)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    all_categories = BlogCategory.objects.annotate(
        posts_count=Count('posts', filter=Q(posts__is_published=True))
    )
    all_tags = BlogTag.objects.annotate(
        posts_count=Count('posts', filter=Q(posts__is_published=True))
    )
    popular_posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')[:3]

    context = {
        'page_obj': page_obj,
        'blog_categories': all_categories,
        'blog_tags': all_tags,
        'popular_posts': popular_posts,
        'selected_category': selected_category_slug,
        'selected_tag': selected_tag_slug,
        'search_query': search_query,
    }
    return render(request, 'blog.html', context)

def contacts(request):
    contact_info = Contact.objects.first()
    parsed_contacts = {}
    if contact_info:
        parsed_contacts['address'] = contact_info.address
        parsed_contacts['phone_numbers'] = _parse_list_from_text(contact_info.phone_numbers)
        parsed_contacts['emails'] = _parse_list_from_text(contact_info.emails)
        parsed_contacts['work_hours'] = contact_info.work_hours
        parsed_contacts['weekend_hours'] = contact_info.weekend_hours
        parsed_contacts['map_url'] = contact_info.map_url
        parsed_contacts['social_media'] = contact_info.social_media

    message_sent_flag = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = form.cleaned_data['subject']

            try:
                send_mail(
                    f'Новое сообщение от {name} ({email}) - {subject}',
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                message_sent_flag = True
                form = ContactForm()
            except Exception as e:
                # Consider logging the error e
                form.add_error(None, "Не удалось отправить сообщение. Попробуйте позже.")
    else:
        form = ContactForm()

    return render(request, 'contacts.html', {
        'contacts': parsed_contacts,
        'form': form,
        'message_sent': message_sent_flag
    })


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def logout_view(request):
    logout(request)
    return redirect('index')