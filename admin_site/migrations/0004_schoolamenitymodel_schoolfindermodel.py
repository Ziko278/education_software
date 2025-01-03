# Generated by Django 5.0 on 2024-12-16 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0003_siteinfomodel_primary_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolAmenityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolFinderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('school_type', models.CharField(max_length=50)),
                ('boarding_type', models.CharField(choices=[('day', 'DAY'), ('boarding', 'BOARDING'), ('combined', 'COMBINED')], max_length=50)),
                ('gender', models.CharField(choices=[('day', 'DAY'), ('boarding', 'BOARDING'), ('combined', 'COMBINED')], max_length=50)),
                ('mobile_1', models.CharField(blank=True, max_length=20, null=True)),
                ('mobile_2', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('lga', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('area', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', models.FileField(upload_to='images/setting/logo')),
                ('short_description', models.TextField(blank=True, null=True)),
                ('main_description', models.TextField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('amenities', models.ManyToManyField(blank=True, to='admin_site.schoolamenitymodel')),
            ],
        ),
    ]
