# Generated by Django 4.0.3 on 2022-04-10 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0004_jobs_delete_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='budget',
            field=models.CharField(choices=[('1', 'Negotiable'), ('2', 'Fixed'), ('3', 'Hourly')], default='1', max_length=10),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='type',
            field=models.CharField(choices=[('1', 'Project'), ('2', 'Jobs')], default='1', max_length=10),
        ),
    ]