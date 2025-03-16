# Generated by Django 5.1.6 on 2025-03-12 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landscape_design_app', '0003_alter_portfolioproject_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price_from', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена от')),
                ('image', models.ImageField(upload_to='service_images/')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
