# Generated by Django 2.1.7 on 2019-02-28 14:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name ')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last Name ')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Address ')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone Number ')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date joined ')),
                ('others', models.TextField(blank=True, null=True, verbose_name='Other Information ')),
            ],
            options={
                'verbose_name': 'Members',
                'verbose_name_plural': 'Members',
            },
        ),
    ]
