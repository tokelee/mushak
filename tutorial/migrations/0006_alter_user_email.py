# Generated by Django 4.2.15 on 2024-08-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0005_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]
