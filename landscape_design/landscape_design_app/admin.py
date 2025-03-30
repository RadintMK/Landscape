from django.contrib import admin
from .models import (
    PortfolioProject, PortfolioImage, PortfolioCategory, PortfolioTag,
    BlogPost, BlogCategory, BlogTag,
    Service, ServiceCategory,
    Contact
)

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author_display', 'created_at', 'is_published')
    list_filter = ('is_published', 'category', 'created_at', 'author')
    search_fields = ('title', 'content', 'preview')
    list_editable = ('is_published',)
    filter_horizontal = ('tags',)
    date_hierarchy = 'created_at'
    autocomplete_fields = ['author', 'category']

    def author_display(self, obj):
        return obj.author.username if obj.author else "N/A"
    author_display.short_description = "Автор"
    author_display.admin_order_field = 'author__username'

    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'author', 'is_published')
        }),
        ('Контент', {
            'fields': ('content', 'preview', 'image')
        }),
        ('Теги', {
            'fields': ('tags',)
        }),
        ('Даты (Авто)', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1
    fields = ('image', 'alt_text', 'order')
    ordering = ('order',)

@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(PortfolioTag)
class PortfolioTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'year', 'area', 'is_published')
    list_filter = ('is_published', 'category', 'year')
    search_fields = ('title', 'description', 'style')
    list_editable = ('is_published',)
    filter_horizontal = ('tags',)
    autocomplete_fields = ['category']
    inlines = [PortfolioImageInline]

    fieldsets = (
         (None, {
             'fields': ('title', 'category', 'is_published')
         }),
         ('Описание и Характеристики', {
             'fields': ('preview', 'description', 'style', 'area', 'duration', 'year')
         }),
         ('Теги', {
             'fields': ('tags',)
         }),
         ('Даты (Авто)', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at',)

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price_from', 'order', 'is_active')
    list_filter = ('is_active', 'category')
    search_fields = ('title', 'description')
    list_editable = ('is_active', 'order', 'price_from')
    autocomplete_fields = ['category']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('address', 'get_phones', 'get_emails', 'work_hours', 'weekend_hours')
    search_fields = ('address', 'phone_numbers', 'emails')

    def get_phones(self, obj):
        return ", ".join(obj.phone_numbers.splitlines()) if obj.phone_numbers else '-'
    get_phones.short_description = 'Телефоны'

    def get_emails(self, obj):
         return ", ".join(obj.emails.splitlines()) if obj.emails else '-'
    get_emails.short_description = 'Email'

    def has_add_permission(self, request):
        return not Contact.objects.exists()

    def has_delete_permission(self, request, obj=None):
         return False