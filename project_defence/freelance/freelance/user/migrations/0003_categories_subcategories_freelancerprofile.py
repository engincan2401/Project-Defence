# Generated by Django 4.0.3 on 2022-03-15 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_customuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, editable=False, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, editable=False, null=True, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.categories')),
            ],
        ),
        migrations.CreateModel(
            name='FreelancerProfile',
            fields=[
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('hourly_rate', models.FloatField()),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.categories')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.subcategories')),
            ],
        ),
    ]