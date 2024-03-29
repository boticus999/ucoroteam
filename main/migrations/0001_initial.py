# Generated by Django 4.2.7 on 2023-11-21 14:08

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
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=10, verbose_name='Сгенерированная ссылка')),
                ('url', models.CharField(max_length=150, verbose_name='Адрес в Интернете')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Имя пользователя')),
            ],
            options={
                'verbose_name': 'ссылка',
                'verbose_name_plural': 'ссылки',
            },
        ),
    ]
