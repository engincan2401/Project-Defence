# Generated by Django 4.0.3 on 2022-03-23 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_delete_foo'),
    ]

    operations = [
        migrations.AddField(
            model_name='employerprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='employerprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='freelancerprofile',
            name='first_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='freelancerprofile',
            name='last_name',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
