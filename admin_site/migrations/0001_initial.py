# Generated by Django 5.0 on 2024-11-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('short_name', models.CharField(max_length=50)),
                ('mobile_1', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', models.FileField(upload_to='images/setting/logo')),
                ('facebook_handle', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram_handle', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter_handle', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
