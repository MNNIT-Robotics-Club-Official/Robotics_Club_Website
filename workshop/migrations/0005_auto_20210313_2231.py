# Generated by Django 3.1.5 on 2021-03-13 17:01

from django.db import migrations, models
import workshop.models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0004_auto_20210313_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='image',
            field=models.ImageField(blank=True, upload_to=workshop.models.get_path),
        ),
    ]
