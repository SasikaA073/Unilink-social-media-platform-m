# Generated by Django 4.0.6 on 2023-08-16 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images/articles/%Y/%m/%d'),
        ),
    ]
