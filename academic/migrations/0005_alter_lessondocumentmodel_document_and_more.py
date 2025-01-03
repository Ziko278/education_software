# Generated by Django 5.0 on 2024-11-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0004_academicsettingmodel_lesson_note_approver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessondocumentmodel',
            name='document',
            field=models.FileField(upload_to='lesson_document'),
        ),
        migrations.AlterField(
            model_name='lessonnotemodel',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='lesson_note'),
        ),
    ]
