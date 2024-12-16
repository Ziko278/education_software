from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.http import HttpResponse
from num2words import num2words
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from school_setting.models import SchoolGeneralInfoModel, SchoolAcademicInfoModel

from student.models import StudentsModel
from student_portal.view.result_view import *


def setup_test():
    if 1:
        return True
    return False


class StudentDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'student_portal/dashboard.html'

    def dispatch(self, *args, **kwargs):
        if setup_test():
            return super(StudentDashboardView, self).dispatch(*args, **kwargs)
        else:
            pass
            # return redirect(reverse('site_info_create'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = self.request.user.profile.student
        return context


class StudentClassMateView(LoginRequiredMixin, TemplateView):
    template_name = 'student_portal/classmate.html'

    def dispatch(self, *args, **kwargs):
        if setup_test():
            return super(StudentClassMateView, self).dispatch(*args, **kwargs)
        else:
            pass
            # return redirect(reverse('site_info_create'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.request.user.profile.student
        context['student'] = student
        context['classmate_list'] = StudentsModel.objects.filter(student_class=student.student_class, class_section=student.class_section).order_by('surname')
        context['class_section_info'] = ClassSectionInfoModel.objects.filter(student_class=student.student_class, section=student.class_section).first()
        return context


class StudentFeeView(SuccessMessageMixin, TemplateView):
    template_name = 'student_portal/fee/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        student = self.request.user.profile.student
        if school_setting.separate_school_section:
            academic_setting = SchoolAcademicInfoModel.objects.filter(type=student.type).first()

        else:
            academic_setting = SchoolAcademicInfoModel.objects.first()

        context['academic_setting'] = academic_setting
        context['student'] = student

        return context

