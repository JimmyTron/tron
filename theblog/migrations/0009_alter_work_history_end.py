# Generated by Django 4.1.6 on 2023-05-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0008_rename_tittle_work_history_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_history',
            name='end',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
