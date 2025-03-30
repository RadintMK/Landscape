from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class BlogCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(unique=True, verbose_name="URL slug", help_text="Уникальная строка для URL (генерируется автоматически, если пусто)")
    description = models.TextField(verbose_name="Описание", blank=True)

    class Meta:
        verbose_name = "Категория блога"
        verbose_name_plural = "Категории блога"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        original_slug = self.slug
        counter = 1
        while BlogCategory.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = f"{original_slug}-{counter}"
            counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class BlogTag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, verbose_name="URL slug", help_text="Уникальная строка для URL (генерируется автоматически, если пусто)")

    class Meta:
        verbose_name = "Тег блога"
        verbose_name_plural = "Теги блога"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        original_slug = self.slug
        counter = 1
        while BlogTag.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = f"{original_slug}-{counter}"
            counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.TextField(verbose_name="Краткое описание", blank=True)
    image = models.ImageField(upload_to='blog/', verbose_name="Изображение", blank=True, null=True)
    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name="Категория"
    )
    tags = models.ManyToManyField(
        BlogTag,
        related_name='posts',
        blank=True,
        verbose_name="Теги"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='blog_posts',
        verbose_name="Автор"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Запись блога"
        verbose_name_plural = "Записи блога"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Contact(models.Model):
    address = models.TextField(verbose_name="Адрес")
    phone_numbers = models.TextField(
        help_text="Номера телефонов через запятую или на новой строке",
        verbose_name="Телефоны",
        blank=True
    )
    emails = models.TextField(
        help_text="Email-адреса через запятую или на новой строке",
        verbose_name="Email",
        blank=True
    )
    work_hours = models.CharField(max_length=100, verbose_name="Часы работы (Пн-Пт)", blank=True)
    weekend_hours = models.CharField(max_length=100, verbose_name="Часы работы (Сб-Вс)", blank=True)
    map_url = models.URLField(verbose_name="Ссылка на карту", blank=True)
    social_media = models.JSONField(
        default=list,
        help_text='Список словарей: [{"url": "ссылка", "icon": "класс иконки fontawesome"}]',
        verbose_name="Соцсети",
        blank=True
    )

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактная информация"

    def __str__(self):
        return "Контактная информация"


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(unique=True, verbose_name="URL slug")

    class Meta:
        verbose_name = "Категория портфолио"
        verbose_name_plural = "Категории портфолио"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
             self.slug = slugify(self.name)
        original_slug = self.slug
        counter = 1
        while PortfolioCategory.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = f"{original_slug}-{counter}"
            counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class PortfolioTag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название тега")
    slug = models.SlugField(unique=True, verbose_name="URL slug", blank=True)

    class Meta:
        verbose_name = "Тег портфолио"
        verbose_name_plural = "Теги портфолио"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
             self.slug = slugify(self.name)
        original_slug = self.slug
        counter = 1
        while PortfolioTag.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = f"{original_slug}-{counter}"
            counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class PortfolioImage(models.Model):
    image = models.ImageField(upload_to='portfolio/', verbose_name="Изображение")
    alt_text = models.CharField(max_length=200, verbose_name="Alt текст (описание)", blank=True)
    project = models.ForeignKey(
        'PortfolioProject',
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name="Проект"
    )
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Порядок")

    class Meta:
        verbose_name = "Изображение портфолио"
        verbose_name_plural = "Изображения портфолио"
        ordering = ['order']

    def __str__(self):
        return self.alt_text or f"Изображение для {self.project.title}"

class PortfolioProject(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание", blank=True)
    preview = models.TextField(verbose_name="Краткое описание", blank=True)
    category = models.ForeignKey(
        PortfolioCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projects',
        verbose_name="Категория"
    )
    tags = models.ManyToManyField(
        PortfolioTag,
        related_name='projects',
        blank=True,
        verbose_name="Теги"
    )
    area = models.DecimalField(
        max_digits=7,
        decimal_places=1,
        verbose_name="Площадь (соток)",
        default=0.0
    )
    style = models.CharField(max_length=100, verbose_name="Стиль", blank=True)
    duration = models.IntegerField(verbose_name="Срок реализации (месяцев)", null=True, blank=True)
    year = models.PositiveIntegerField(verbose_name="Год", null=True, blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Проект портфолио"
        verbose_name_plural = "Проекты портфолио"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_first_image_url(self):
        first_image = self.images.order_by('order').first()
        if first_image and first_image.image:
            return first_image.image.url
        return None

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(unique=True, verbose_name="URL slug")

    class Meta:
        verbose_name = "Категория услуг"
        verbose_name_plural = "Категории услуг"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
             self.slug = slugify(self.name)
        original_slug = self.slug
        counter = 1
        while ServiceCategory.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = f"{original_slug}-{counter}"
            counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание", blank=True)
    price_from = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена от", null=True, blank=True)
    image = models.ImageField(upload_to='service_images/', verbose_name="Изображение", blank=True, null=True)
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='services',
        verbose_name="Категория"
    )
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Порядок")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title