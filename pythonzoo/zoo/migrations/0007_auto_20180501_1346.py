# Generated by Django 2.0.4 on 2018-05-01 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0006_zoo_logofilename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='zoo',
        ),
        migrations.AddField(
            model_name='animal',
            name='dietDescription',
            field=models.TextField(help_text='Enter a description of the Diet', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='habitatDescription',
            field=models.TextField(help_text='Enter a description of the Habitat', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='imageFileName',
            field=models.CharField(help_text='Enter logo file name', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='soundFileName',
            field=models.CharField(help_text='Enter sound file name', max_length=200, null=True),
        ),
    ]
