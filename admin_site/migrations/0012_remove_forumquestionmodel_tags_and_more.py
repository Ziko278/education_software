# Generated by Django 5.0 on 2024-12-20 12:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0011_alter_forumquestionmodel_privacy'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumquestionmodel',
            name='tags',
        ),
        migrations.AlterField(
            model_name='forumquestionmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='schoolfindermodel',
            name='boarding_type',
            field=models.CharField(blank=True, choices=[('day', 'DAY'), ('boarding', 'BOARDING'), ('combined', 'COMBINED')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='schoolfindermodel',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='schoolfindermodel',
            name='lga',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='schoolfindermodel',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]