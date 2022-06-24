# Generated by Django 4.0.5 on 2022-06-23 19:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spaces', '0015_space_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=300)),
                ('Content', models.TextField()),
                ('username', models.CharField(max_length=255)),
                ('published_on', models.DateTimeField(default=datetime.datetime(2022, 6, 24, 1, 10, 27, 390159))),
                ('Space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spaces.space')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
