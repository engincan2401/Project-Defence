# Generated by Django 4.0.3 on 2022-03-15 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_subcategories_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategories',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.categories'),
        ),
    ]
