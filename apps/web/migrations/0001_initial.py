# Generated by Django 2.2.20 on 2022-10-31 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=70)),
                ('message', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')], default='Pending', max_length=30)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=70)),
            ],
            options={
                'verbose_name_plural': 'Subscribers',
                'db_table': 'subscribers',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=70, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('headshot', models.ImageField(blank=True, null=True, upload_to='headshots')),
                ('visible', models.BooleanField(default=False)),
                ('github_url', models.CharField(blank=True, max_length=200, null=True)),
                ('linkedin_url', models.CharField(blank=True, max_length=200, null=True)),
                ('personal_website', models.CharField(blank=True, max_length=200, null=True)),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='bg-images')),
                ('team_type', models.CharField(choices=[('Core Team', 'Core Team'), ('Contributor', 'Contributor')], max_length=50)),
                ('position', models.PositiveIntegerField(default=0)),
            ],
            options={
                'db_table': 'teams',
            },
        ),
    ]
