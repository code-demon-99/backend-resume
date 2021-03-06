# Generated by Django 3.2 on 2022-01-29 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('tech_stack', models.CharField(max_length=300)),
                ('git_repo_link', models.URLField(blank=True, null=True)),
                ('project_link', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('tags', models.JSONField()),
            ],
        ),
    ]
