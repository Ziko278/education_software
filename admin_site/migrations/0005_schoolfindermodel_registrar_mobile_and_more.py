# Generated by Django 5.0 on 2024-12-16 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0004_schoolamenitymodel_schoolfindermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolfindermodel',
            name='registrar_mobile',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='schoolfindermodel',
            name='registrar_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='schoolfindermodel',
            name='registrar_position',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='schoolfindermodel',
            name='school_head_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='schoolfindermodel',
            name='school_owner_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='schoolfindermodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]