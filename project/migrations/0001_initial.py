# Generated by Django 3.1.5 on 2023-07-05 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import project.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('aim', models.TextField(max_length=200)),
                ('github', models.URLField(blank=True)),
                ('vidlink', models.URLField(blank=True)),
                ('detail', models.TextField()),
                ('overview', models.TextField(blank=True)),
                ('status', models.IntegerField(choices=[(0, 'Ongoing'), (1, 'Completed'), (2, 'Abandoned')], default=0)),
                ('comp_and_tech', models.CharField(default=None, max_length=250)),
                ('image', models.ImageField(blank=True, upload_to=project.models.get_path)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='ShareKey',
            fields=[
                ('location', models.TextField()),
                ('token', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('expiration_seconds', models.BigIntegerField()),
                ('project', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sharelink', to='project.project')),
            ],
        ),
    ]
