# Generated by Django 3.1.5 on 2021-02-23 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0002_auto_20210220_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]