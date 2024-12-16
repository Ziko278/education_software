# Generated by Django 5.0 on 2024-11-15 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0003_initial'),
        ('human_resource', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicsettingmodel',
            name='lesson_note_approver',
            field=models.ManyToManyField(blank=True, related_name='lesson_note_approver', to='human_resource.staffmodel'),
        ),
        migrations.AddField(
            model_name='lessonnotemodel',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='lessonnotemodel',
            name='decline_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lessonnotemodel',
            name='scheduled_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lessonnotemodel',
            name='scheduled_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lessonnotemodel',
            name='status',
            field=models.CharField(default='ll', max_length=20),
            preserve_default=False,
        ),
    ]