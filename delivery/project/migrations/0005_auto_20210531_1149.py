# Generated by Django 3.2 on 2021-05-31 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_rename_steamed_users_steamed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AlterField(
            model_name='users',
            name='nickname',
            field=models.CharField(default=1, max_length=20, primary_key=True, serialize=False),
        ),
    ]
