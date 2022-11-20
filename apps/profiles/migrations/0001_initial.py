# Generated by Django 4.1.3 on 2022-11-19 05:43

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.FileField(blank=True, null=True, upload_to='', verbose_name='Аватар')),
                ('bio', models.TextField(blank=True, max_length=500, null=True, verbose_name='О себе')),
                ('city', models.CharField(blank=True, max_length=30, null=True, verbose_name='Город')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('gender', models.CharField(choices=[['male', 'Мужской'], ['female', 'Женский']], default='male', max_length=10, verbose_name='Пол')),
                ('relationship', models.CharField(choices=[['none', 'Не определенно'], ['single', 'Холост'], ['in_a_rel', 'В отношениях'], ['engaged', 'Помолвлен(а)'], ['married', 'Женат/Замужем'], ['in_love', 'Влюблен(а)'], ['complicated', 'Все сложно']], default='none', max_length=20, verbose_name='Статус отношений')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('text', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Текст')),
                ('image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Картинка')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-datetime'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('text', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Текст')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='profiles.post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Комент',
                'verbose_name_plural': 'Коментарий',
                'ordering': ['datetime'],
            },
        ),
    ]
