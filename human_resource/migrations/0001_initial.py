# Generated by Django 5.0 on 2024-11-14 09:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HRSettingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto_generate_staff_id', models.BooleanField(default=True)),
                ('type', models.CharField(blank=True, choices=[('pri', 'PRIMARY'), ('sec', 'SECONDARY')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='StaffIDGeneratorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_id', models.IntegerField()),
                ('last_staff_id', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, choices=[('s', 'SUCCESS'), ('f', 'FAIL')], default='f', max_length=10)),
                ('type', models.CharField(blank=True, choices=[('pri', 'PRIMARY'), ('sec', 'SECONDARY')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, choices=[('pri', 'PRIMARY'), ('sec', 'SECONDARY')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department_updated_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PositionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, choices=[('pri', 'PRIMARY'), ('sec', 'SECONDARY')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='human_resource.departmentmodel')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='position_updated_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StaffModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('image', models.FileField(blank=True, null=True, upload_to='images/staff_images')),
                ('residential_address', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('lga', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=10)),
                ('marital_status', models.CharField(blank=True, choices=[('single', 'SINGLE'), ('married', 'MARRIED'), ('widowed', 'WIDOWED'), ('separated', 'SEPARATED')], max_length=30, null=True)),
                ('religion', models.CharField(blank=True, choices=[('christianity', 'CHRISTIANITY'), ('islam', 'ISLAM'), ('others', 'OTHERS')], max_length=30, null=True)),
                ('staff_id', models.CharField(blank=True, max_length=100, null=True)),
                ('employment_date', models.DateField(blank=True, null=True)),
                ('cv', models.FileField(blank=True, null=True, upload_to='staff/cv')),
                ('salary', models.BigIntegerField(blank=True, default=0, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('account_name', models.CharField(blank=True, max_length=100, null=True)),
                ('account_number', models.CharField(blank=True, max_length=50, null=True)),
                ('blood_group', models.CharField(blank=True, choices=[('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b-', 'B-'), ('ab+', 'AB+'), ('ab-', 'AB-'), ('o+', 'O+'), ('o-', 'O-')], max_length=20, null=True)),
                ('genotype', models.CharField(blank=True, choices=[('aa', 'AA'), ('as', 'AS'), ('ac', 'AC'), ('ss', 'SS')], max_length=20, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('health_issues', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, default='active', max_length=30)),
                ('can_teach', models.BooleanField(blank=True, default=True)),
                ('barcode', models.FileField(blank=True, null=True, upload_to='barcode/staff')),
                ('type', models.CharField(blank=True, choices=[('pri', 'PRIMARY'), ('sec', 'SECONDARY')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_staffs', to='human_resource.departmentmodel')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position_staffs', to='human_resource.positionmodel')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staff_updated_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='departmentmodel',
            constraint=models.UniqueConstraint(fields=('name', 'type'), name='unique_dept_name_type_combo'),
        ),
        migrations.AddConstraint(
            model_name='positionmodel',
            constraint=models.UniqueConstraint(fields=('name', 'department', 'type'), name='unique_dept_name_and_dept_and_type_combo'),
        ),
        migrations.AddConstraint(
            model_name='staffmodel',
            constraint=models.UniqueConstraint(fields=('staff_id', 'type'), name='unique_staff_id'),
        ),
    ]