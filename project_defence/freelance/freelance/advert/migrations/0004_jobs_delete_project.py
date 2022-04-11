# Generated by Django 4.0.3 on 2022-03-27 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advert', '0003_project_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('1', 'Проект'), ('2', 'Работа')], default='1', max_length=10)),
                ('description', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('budget', models.CharField(choices=[('1', 'По договаряне'), ('2', 'Фиксирано')], default='1', max_length=10)),
                ('price', models.FloatField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, editable=False, null=True, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advert.categories')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
