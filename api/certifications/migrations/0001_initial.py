# Generated by Django 3.2 on 2022-01-30 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5000)),
                ('issuing_organization', models.CharField(max_length=5000)),
                ('do_expire', models.BooleanField(default=False)),
                ('issue_date', models.DateField()),
                ('expiration_certificate', models.DateField()),
                ('credential_ID', models.CharField(max_length=500)),
                ('credential_url', models.URLField(max_length=1000)),
            ],
        ),
    ]
