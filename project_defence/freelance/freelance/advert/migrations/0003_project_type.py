# Generated by Django 4.0.3 on 2022-03-27 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0002_project_user_alter_project_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('1', 'По договаряне'), ('2', 'Фиксирано')], default='1', max_length=10),
        ),
    ]
