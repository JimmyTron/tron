# Generated by Django 4.1.6 on 2023-05-24 11:27

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0005_alter_project_kaggle_url_alter_project_web_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Work_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField(blank=True, null=True)),
                ('End', models.DateField(auto_now=True, null=True)),
                ('tittle', models.CharField(max_length=100)),
                ('Description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('company', models.CharField(max_length=100)),
                ('created_at_date', models.DateField(auto_now_add=True)),
                ('skills', models.ManyToManyField(to='theblog.skill')),
            ],
        ),
    ]
