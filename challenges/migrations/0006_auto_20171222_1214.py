# Generated by Django 2.0 on 2017-12-22 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0005_auto_20171222_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='description',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='challenges',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]