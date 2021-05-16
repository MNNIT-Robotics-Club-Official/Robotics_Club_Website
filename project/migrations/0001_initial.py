from django.conf import settings
from django.db import migrations, models
import project.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
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
                ('status', models.IntegerField(choices=[(0, 'Ongoing'), (1, 'Completed'), (2, 'Abandoned')], default=0)),
                ('comp_and_tech', models.TextField(default=None, max_length=250)),
                ('image', models.ImageField(default='default-project.png', upload_to=project.models.get_path)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]