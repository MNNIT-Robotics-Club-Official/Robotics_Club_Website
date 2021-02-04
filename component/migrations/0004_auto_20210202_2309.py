# Generated by Django 3.0.3 on 2021-02-02 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0003_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='type',
            field=models.IntegerField(choices=[(0, 'Miscellaneous'), (1, 'Board')], default=0),
        ),
        migrations.AddField(
            model_name='request',
            name='reason',
            field=models.TextField(default='', max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='time_confirmation',
            field=models.TimeField(default='21:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='user_confirmation',
            field=models.BooleanField(default=False),
        ),
    ]