# Generated by Django 3.1.5 on 2021-03-10 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='branch',
            field=models.IntegerField(blank=True, choices=[(0, 'Biotechnology'), (1, 'Civil Engineering'), (2, 'Electrical Engineering'), (3, 'Mechanical Engineering'), (4, 'Computer Science and Engineering'), (5, 'Electronics and Communication Engineering'), (6, 'Production and Industrial Engineering'), (8, 'Information Technology'), (9, 'Chemical Engineering')], null=True),
        ),
    ]
