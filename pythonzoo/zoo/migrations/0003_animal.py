# Generated by Django 2.0.4 on 2018-04-25 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0002_exhibit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Animal Name', max_length=200)),
                ('exhibit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zoo.Exhibit')),
            ],
        ),
    ]
