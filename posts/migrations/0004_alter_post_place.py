# Generated by Django 3.2.25 on 2024-05-11 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20240508_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='place',
            field=models.CharField(max_length=150),
        ),
    ]