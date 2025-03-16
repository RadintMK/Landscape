from django.contrib import admin
from .models import PortfolioProject, BlogPost, Service

admin.site.register(PortfolioProject)
admin.site.register(BlogPost)
admin.site.register(Service)