# Generated by Django 2.0 on 2017-12-21 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenges',
            name='solved_by',
        ),
    ]