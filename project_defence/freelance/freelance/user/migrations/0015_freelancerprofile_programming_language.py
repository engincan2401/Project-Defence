# Generated by Django 4.0.3 on 2022-04-10 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_customuser_last_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancerprofile',
            name='programming_language',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
