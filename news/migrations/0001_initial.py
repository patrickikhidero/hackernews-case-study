# Generated by Django 3.2.5 on 2021-12-20 12:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('url', models.URLField(blank=True)),
                ('text', models.TextField(blank=True)),
                ('score', models.IntegerField()),
                ('is_from_api', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
