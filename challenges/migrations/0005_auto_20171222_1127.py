# Generated by Django 2.0 on 2017-12-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0004_challenges_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='files',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
    ]