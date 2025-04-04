# Generated by Django 5.1.6 on 2025-03-30 14:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landscape_design_app', '0006_auto_20250323_2211'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
                ('slug', models.SlugField(unique=True, verbose_name='URL slug')),
            ],
            options={
                'verbose_name': 'Категория блога',
                'verbose_name_plural': 'Категории блога',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название тега')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='URL slug')),
            ],
            options={
                'verbose_name': 'Тег блога',
                'verbose_name_plural': 'Теги блога',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('phone_numbers', models.TextField(blank=True, help_text='Номера телефонов через запятую или на новой строке', verbose_name='Телефоны')),
                ('emails', models.TextField(blank=True, help_text='Email-адреса через запятую или на новой строке', verbose_name='Email')),
                ('work_hours', models.CharField(blank=True, max_length=100, verbose_name='Часы работы (Пн-Пт)')),
                ('weekend_hours', models.CharField(blank=True, max_length=100, verbose_name='Часы работы (Сб-Вс)')),
                ('map_url', models.URLField(blank=True, verbose_name='Ссылка на карту')),
                ('social_media', models.JSONField(blank=True, default=list, help_text='Список словарей: [{"url": "ссылка", "icon": "класс иконки fontawesome"}]', verbose_name='Соцсети')),
            ],
            options={
                'verbose_name': 'Контактная информация',
                'verbose_name_plural': 'Контактная информация',
            },
        ),
        migrations.CreateModel(
            name='PortfolioCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
                ('slug', models.SlugField(unique=True, verbose_name='URL slug')),
            ],
            options={
                'verbose_name': 'Категория портфолио',
                'verbose_name_plural': 'Категории портфолио',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PortfolioTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название тега')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='URL slug')),
            ],
            options={
                'verbose_name': 'Тег портфолио',
                'verbose_name_plural': 'Теги портфолио',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
                ('slug', models.SlugField(unique=True, verbose_name='URL slug')),
            ],
            options={
                'verbose_name': 'Категория услуг',
                'verbose_name_plural': 'Категории услуг',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-created_at'], 'verbose_name': 'Запись блога', 'verbose_name_plural': 'Записи блога'},
        ),
        migrations.AlterModelOptions(
            name='portfolioproject',
            options={'ordering': ['-created_at'], 'verbose_name': 'Проект портфолио', 'verbose_name_plural': 'Проекты портфолио'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['order', 'title'], 'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.RemoveField(
            model_name='portfolioproject',
            name='image',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog_posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='preview',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='portfolioproject',
            name='area',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=7, verbose_name='Площадь (соток)'),
        ),
        migrations.AddField(
            model_name='portfolioproject',
            name='duration',
            field=models.IntegerField(blank=True, null=True, verbose_name='Срок реализации (месяцев)'),
        ),
        migrations.AddField(
            model_name='portfolioproject',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AddField(
            model_name='portfolioproject',
            name='preview',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='portfolioproject',
            name='style',
            field=models.CharField(blank=True, max_length=100, verbose_name='Стиль'),
        ),
        migrations.AddField(
            model_name='portfolioproject',
            name='year',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Год'),
        ),
        migrations.AddField(
            model_name='service',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(verbose_name='Содержимое'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='portfolioproject',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='portfolioproject',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='portfolioproject',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название проекта'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='service_images/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='service',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активна'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price_from',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена от'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название услуги'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='landscape_design_app.blogcategory', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='landscape_design_app.blogtag', verbose_name='Теги'),
        ),
        migrations.AddField(
            model_name='portfolioproject',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='landscape_design_app.portfoliocategory', verbose_name='Категория'),
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio/', verbose_name='Изображение')),
                ('alt_text', models.CharField(blank=True, max_length=200, verbose_name='Alt текст (описание)')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='landscape_design_app.portfolioproject', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Изображение портфолио',
                'verbose_name_plural': 'Изображения портфолио',
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='portfolioproject',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='projects', to='landscape_design_app.portfoliotag', verbose_name='Теги'),
        ),
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services', to='landscape_design_app.servicecategory', verbose_name='Категория'),
        ),
    ]
