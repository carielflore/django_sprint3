# Generated by Django 3.2.16 on 2025-06-11 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Текст')),
                ('slug', models.SlugField(unique=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='blog.category', verbose_name='Категория')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='blog.location', verbose_name='Местоположение')),
            ],
        ),
    ]
