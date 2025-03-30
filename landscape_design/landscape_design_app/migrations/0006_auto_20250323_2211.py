from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('landscape_design_app', '0005_auto_20250323_2207'), 
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(upload_to='blog/', default='static/images/hero.png'),
        ),
    ]