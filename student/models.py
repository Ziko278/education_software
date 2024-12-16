from django.db import models
from academic.models import ClassesModel, ClassSectionModel, SubjectGroupModel
from django.contrib.auth.models import User, Group
from user_management.models import UserProfileModel
from school_setting.models import SchoolSettingModel, SessionModel, SchoolAcademicInfoModel, SchoolGeneralInfoModel
import random
from io import BytesIO
from django.core.files.base import ContentFile
from django.apps import apps


class ParentsModel(models.Model):
    """   """
    TITLE = (
        ('MR', 'MR'), ('MRS', 'MRS'), ('MISS', 'MISS'), ('MS', 'MS'), ('MALLAM', 'MALLAM'), ('DOC', 'DOC'),
        ('BARR', 'BARR'), ('PST', 'PST'), ('PROF', 'PROF'),  ('ENGR', 'ENGR'), ('ALHAJI', 'ALHAJI'), ('HAJIYAH', 'HAJIYAH')
    )
    title = models.CharField(max_length=10, choices=TITLE)
    surname = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)

    image = models.FileField(blank=True, null=True, upload_to='images/parent_images')
    residential_address = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    occupation = models.CharField(max_length=100, null=True, blank=True)
    office_address = models.CharField(max_length=200, null=True, blank=True)
    office_mobile = models.CharField(max_length=20, null=True, blank=True)
    parent_id = models.CharField(max_length=50, blank=True, unique=True)

    state = models.CharField(max_length=100, null=True, blank=True)
    lga = models.CharField(max_length=100, null=True, blank=True)
    RELIGION = (
        ('christianity', 'CHRISTIANITY'), ('islam', 'ISLAM'), ('others', 'OTHERS')
    )
    religion = models.CharField(max_length=30, choices=RELIGION, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    GENDER = (
        ('MALE', 'MALE'), ('FEMALE', 'FEMALE')
    )
    gender = models.CharField(max_length=10, choices=GENDER)
    MARITAL_STATUS = (
        ('single', 'SINGLE'), ('married', 'MARRIED'), ('widowed', 'WIDOWED'), ('separated', 'SEPARATED')
    )
    marital_status = models.CharField(max_length=30, choices=MARITAL_STATUS, null=True, blank=True)

    registration_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=15, blank=True, default='active')
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='parent_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        if self.middle_name:
            return self.title.title() + ' ' + self.surname.title() + ' ' + self.middle_name.title() + ' ' + self.last_name.title()
        else:
            return self.title.title() + ' ' + self.surname.title() + ' ' + self.last_name.title()

    def number_of_ward(self):
        return StudentsModel.objects.filter(parent=self).count()

    def active_wards_count(self):
        return StudentsModel.objects.filter(parent=self, status='active').count()

    def save(self, *args, **kwargs):
        setting = SchoolGeneralInfoModel.objects.first()
        if setting.school_type == 'mix' and setting.separate_school_section:
            parent_setting = StudentSettingModel.objects.filter(type=self.type).first()
        else:
            parent_setting = StudentSettingModel.objects.first()

        if parent_setting.auto_generate_parent_id and not self.parent_id:
            if setting.school_type == 'mix' and setting.separate_school_section:
                last_parent = ParentIDGeneratorModel.objects.filter(type=self.type, status='s').last()
            else:
                last_parent = ParentIDGeneratorModel.objects.filter(status='s').last()
            if last_parent:
                parent_id = str(int(last_parent.last_id) + 1)
            else:
                parent_id = str(1)
            while True:
                gen_id = parent_id
                if setting.school_type == 'mix':
                    parent_id = 'p' + self.type[0] + '-' + parent_id.rjust(7, '0')
                else:
                    parent_id = 'p' + parent_id.rjust(8, '0')
                parent_exist = ParentsModel.objects.filter(parent_id=parent_id).first()
                if not parent_exist:
                    break
                else:
                    parent_id = str(int(gen_id) + 1)
            self.parent_id = parent_id

            generate_id = ParentIDGeneratorModel.objects.create(last_id=gen_id, last_parent_id=self.parent_id,
                                                                status='f',
                                                                type=self.type)
            generate_id.save()

        else:
            user_profile = UserProfileModel.objects.get(parent_id=self.id)
            user = user_profile.user
            if self.email:
                user.email = self.email
            user.save()

        super(ParentsModel, self).save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['parent_id', 'type'],
                name='unique_parent_id'
            )
        ]


class StudentsModel(models.Model):
    """"""
    surname = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=50, blank=True, null=True)
    class_number = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    subject_group = models.ForeignKey(SubjectGroupModel, null=True, blank=True, on_delete=models.CASCADE)
    GENDER = (
        ('MALE', 'MALE'), ('FEMALE', 'FEMALE')
    )
    gender = models.CharField(max_length=10, choices=GENDER)
    state = models.CharField(max_length=100, null=True, blank=True)
    lga = models.CharField(max_length=100, null=True, blank=True)
    RELIGION = (
        ('christianity', 'CHRISTIANITY'), ('islam', 'ISLAM'), ('others', 'OTHERS')
    )
    religion = models.CharField(max_length=30, choices=RELIGION, null=True, blank=True)
    image = models.FileField(blank=True, null=True, upload_to='images/student_images')
    mobile = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    BG = (
        ('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b-', 'B-'), ('ab+', 'AB+'), ('ab-', 'AB-'), ('o+', 'O+'),
        ('o-', 'O-'),
    )
    blood_group = models.CharField(max_length=20, choices=BG, null=True, blank=True)
    GENOTYPE = (
        ('aa', 'AA'), ('as', 'AS'), ('ac', 'AC'), ('ss', 'SS')
    )
    genotype = models.CharField(max_length=20, choices=GENOTYPE, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    health_issue = models.TextField(null=True, blank=True)
    student_class = models.ForeignKey(ClassesModel, null=True, on_delete=models.CASCADE)
    class_section = models.ForeignKey(ClassSectionModel, null=True, on_delete=models.CASCADE)
    parent = models.ForeignKey(ParentsModel, on_delete=models.CASCADE, blank=True, related_name='students')
    RELATIONSHIP_WITH_PARENT = (
        ('father', 'FATHER'), ('mother', 'MOTHER'), ('sister', 'SISTER'), ('brother', 'BROTHER'), ('uncle', 'UNCLE'),
        ('aunty', 'AUNTY'), ('pastor', 'PASTOR'), ('others', 'OTHERS')
    )
    relationship_with_parent = models.CharField(max_length=20, choices=RELATIONSHIP_WITH_PARENT)

    registration_date = models.DateField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, default='active')
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='student_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        if self.middle_name:
            return self.surname + ' ' + self.middle_name + ' ' + self.last_name
        else:
            return self.surname + ' ' + self.last_name

    def save(self, *args, **kwargs):
        setting = SchoolGeneralInfoModel.objects.first()
        if setting.school_type == 'mix' and setting.separate_school_section:
            student_setting = StudentSettingModel.objects.filter(type=self.type).first()
            academic_info = SchoolAcademicInfoModel.objects.filter(type=self.type).first()
        else:
            student_setting = StudentSettingModel.objects.first()
            academic_info = SchoolAcademicInfoModel.objects.filter().first()
        session = str(academic_info.session.start_year)[-2:]

        if student_setting.auto_generate_student_id and not self.registration_number:
            if setting.school_type == 'mix' and setting.separate_school_section:
                last_student = StudentIDGeneratorModel.objects.filter(type=self.type, session=academic_info.session,
                                                                      status='s').last()
            else:
                last_student = StudentIDGeneratorModel.objects.filter(session=academic_info.session, status='s').last()
            if last_student:
                student_id = str(int(last_student.last_id) + 1)
            else:
                student_id = str(1)
            while True:
                gen_id = student_id
                if setting.school_type == 'mix':
                    student_id = self.type[0] + session + '-' + student_id.rjust(4, '0')
                else:
                    student_id = session + '-' + student_id.rjust(4, '0')
                student_exist = StudentsModel.objects.filter(registration_number=student_id).first()
                if not student_exist:
                    break
                else:
                    student_id = str(int(gen_id) + 1)
            self.registration_number = student_id

            generate_id = StudentIDGeneratorModel.objects.create(last_id=gen_id, session=academic_info.session,
                                                                 last_student_id=self.registration_number,
                                                                 status='f', type=self.type)
            generate_id.save()

        else:
            if self.id:
                try:
                    user_profile = UserProfileModel.objects.get(student_id=self.id)
                    user = user_profile.user
                    user.username = self.registration_number
                    if self.email:
                        user.email = self.email
                    user.save()
                except UserProfileModel.DoesNotExist:
                    username = self.registration_number
                    email = self.email
                    password = User.objects.make_random_password(length=8)
                    try:
                        user = User.objects.get(username=self.registration_number)
                    except User.DoesNotExist:
                        user = User.objects.create_user(username=username, email=email, password=password)
                        user.save()

                    user_profile = UserProfileModel.objects.create(user=user, student=self, type=self.type,
                                                                   default_password=password, reference='student', reference_id=self.id)
                    user_profile.save()

        super(StudentsModel, self).save(*args, **kwargs)

    def no_in_class(self):
            return StudentsModel.objects.filter(student_class=self.student_class, class_section=self.class_section).count()


class StudentAcademicRecordModel(models.Model):
    student = models.OneToOneField(StudentsModel, on_delete=models.CASCADE, related_name='student_academic_record')
    entry_class = models.ForeignKey(ClassesModel, on_delete=models.SET_NULL, null=True)
    entry_class_section = models.ForeignKey(ClassSectionModel, on_delete=models.SET_NULL, null=True)
    entry_session = models.ForeignKey(SessionModel, on_delete=models.SET_NULL, null=True, related_name='entry_session')
    entry_term = models.CharField(max_length=20)
    previous_classes = models.JSONField(null=True, blank=True)
    attendance_record = models.JSONField(null=True, blank=True)
    date_of_graduation = models.DateField(null=True)
    session_of_graduation = models.ForeignKey(SessionModel, on_delete=models.SET_NULL, null=True)
    exit_mode = models.CharField(max_length=20, null=True)
    session_of_departure = models.ForeignKey(SessionModel, on_delete=models.SET_NULL, related_name='departure',
                                             null=True)
    term_of_departure = models.CharField(max_length=20, null=True)
    entry_age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.student.surname.title(), self.student.last_name.title())


class StudentIDGeneratorModel(models.Model):
    last_id = models.IntegerField()
    last_student_id = models.CharField(max_length=100, null=True, blank=True)
    session = models.ForeignKey(SessionModel, on_delete=models.CASCADE, null=True, blank=True)
    STATUS = (
        ('s', 'SUCCESS'), ('f', 'FAIL')
    )
    status = models.CharField(max_length=10, choices=STATUS, blank=True, default='f')

    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)


class ParentIDGeneratorModel(models.Model):
    last_id = models.IntegerField()
    last_parent_id = models.CharField(max_length=100, null=True, blank=True)
    STATUS = (
        ('s', 'SUCCESS'), ('f', 'FAIL')
    )
    status = models.CharField(max_length=10, choices=STATUS, blank=True, default='f')

    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)


class StudentSettingModel(models.Model):
    auto_generate_student_id = models.BooleanField(default=True)
    auto_generate_parent_id = models.BooleanField(default=True)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
