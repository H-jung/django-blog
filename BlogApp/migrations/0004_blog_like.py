# Generated by Django 3.0.6 on 2020-07-06 06:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogApp', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='like',
            field=models.ManyToManyField(related_name='likers', to=settings.AUTH_USER_MODEL),
        ),
    ]
