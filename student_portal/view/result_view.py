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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from school_setting.models import SchoolGeneralInfoModel, SchoolAcademicInfoModel
from school_setting.models import SchoolGeneralInfoModel
from student.models import StudentsModel
from result.models import *
from academic.models import *


@login_required
def current_term_result(request, pk):
    student = StudentsModel.objects.get(pk=pk)
    result_type = request.GET.get('type', None)
    school_setting = SchoolGeneralInfoModel.objects.first()

    if school_setting.separate_school_section:
        result_setting = ResultSettingModel.objects.filter(type=request.user.profile.type).first()
        academic_setting = SchoolAcademicInfoModel.objects.filter(type=request.user.profile.type).first()
        academic_info = AcademicSettingModel.objects.filter(type=request.user.profile.type).first()
    else:
        result_setting = ResultSettingModel.objects.first()
        academic_setting = SchoolAcademicInfoModel.objects.first()
        academic_info = AcademicSettingModel.objects.first()

    session = academic_setting.session
    term = academic_setting.term

    result_is_published = False
    if result_setting.result_status == 'published':
        result_is_published = True

    student_class = student.student_class
    class_section = student.class_section
    school_setting = SchoolGeneralInfoModel.objects.first()
    result = ResultModel.objects.filter(term=term, session=session, student=student).first()
    behaviour_category_list = ResultBehaviourCategoryModel.objects.all().order_by('name')
    behaviour_result = ResultBehaviourComputeModel.objects.filter(term=term, session=session,
                                                                  student=student).first()

    result_stat = ResultStatisticModel.objects.filter(term=term, session=session, student_class=student_class,
                                                      class_section=class_section).first()

    result_remark = ResultRemarkModel.objects.filter(term=term, session=session,
                                                     student=student).first()
    total_score = 0
    number_of_course = 0
    average = 0
    total_lowest = 0
    class_minimum = 0
    if result:
        for key, student_result in result.result.items():
            student_result['highest_in_class'] = result_stat.result_statistic[key]['highest_in_class']
            student_result['lowest_in_class'] = result_stat.result_statistic[key]['lowest_in_class']
            total_lowest += result_stat.result_statistic[key]['lowest_in_class']

        number_of_course = len(result.result.items())
        class_minimum = round((total_lowest / (100 * number_of_course)) * 100) if number_of_course else 0
    if result:
        for key, value in result.result.items():
            total_score += value['total']
        average = round((total_score / (100 * number_of_course)) * 100) if number_of_course else 0

    if result:
        for key, student_result in result.result.items():
            student_result['highest_in_class'] = result_stat.result_statistic[key].get('highest_in_class', '')
            student_result['lowest_in_class'] = result_stat.result_statistic[key].get('lowest_in_class', '')
            student_result['average_score'] = result_stat.result_statistic[key].get('average_score', '')
            student_result['midterm_highest_in_class'] = result_stat.result_statistic[key].get(
                'midterm_highest_in_class', '')
            student_result['midterm_lowest_in_class'] = result_stat.result_statistic[key].get('midterm_lowest_in_class',
                                                                                              '')
            student_result['midterm_average_score'] = result_stat.result_statistic[key].get('midterm_average_score', '')
            student_result['number_of_student'] = result_stat.result_statistic[key].get('number_of_students', '')

    if school_setting.separate_school_section:
        field_list = ResultFieldModel.objects.filter(student_class__in=[student_class]).filter(
            class_section__in=[class_section], type=request.user.profile.type).order_by('order')
        grade_list = ResultGradeModel.objects.filter(student_class__in=[student_class],
                                                     class_section__in=[class_section],
                                                     type=request.user.profile.type).order_by('order')
        behaviour_category_list = ResultBehaviourCategoryModel.objects.filter(type=request.user.profile.type).order_by(
            'name')
    else:
        field_list = ResultFieldModel.objects.filter(student_class__in=[student_class]).filter(
            class_section__in=[class_section]).order_by('order')
        grade_list = ResultGradeModel.objects.filter(student_class__in=[student_class]).filter(
            class_section__in=[class_section]).order_by('order')
    class_detail = ClassSectionInfoModel.objects.filter(student_class=student_class, section=class_section).first()

    if student.subject_group:
        subject_list = student.subject_group.subjects.all()
    else:
        class_detail = ClassSectionInfoModel.objects.filter(student_class=student_class, section=class_section).first()
        if class_detail:
            subject_list = class_detail.subjects
        else:
            subject_list = []

    midterm_max = 0
    for field in field_list:
        if field.mid_term:
            midterm_max += field.max_mark
    context = {}
    if student_class.result_type == 'text' or student_class.result_type == 'mix':
        text_result = TextBasedResultModel.objects.filter(term=term, session=session, student=student).first()
        if school_setting.separate_school_section:
            result_category_list = TextResultCategoryModel.objects.filter(term=term, session=session,
                                                                          type=request.user.profile.type, student_class__in=[student.student_class.id],
                                                               class_section__in=[student.class_section.id]).order_by(
                'order')
            result_field_list = TextResultModel.objects.filter(type=request.user.profile.type,
                                                               student_class__in=[student.student_class.id],
                                                               class_section__in=[student.class_section.id]).order_by(
                'order')
        else:
            result_category_list = TextResultCategoryModel.objects.filter(term=term, session=session, student_class__in=[student.student_class.id],
                                                               class_section__in=[student.class_section.id]).order_by('order')
            result_field_list = TextResultModel.objects.filter(student_class__in=[student.student_class.id],
                                                               class_section__in=[student.class_section.id]).order_by(
                'order')

        context.update({
            'result_list': text_result,
            'result': result,
            'academic_setting': academic_setting,
            'result_category_list': result_category_list,
            'result_field_list': result_field_list,
            'general_setting': SchoolGeneralInfoModel.objects.first(),
            'total_score': total_score,
            'number_of_course': number_of_course,
            'average_score': average,
            'class_minimum': class_minimum,
            'result_type': result_type,
            'midterm_max': midterm_max,
        })
        # return render(request, 'result/result/text_result/main_result_template.html', context=context)

    context.update({
        'student': student,
        'academic_setting': academic_setting,
        'academic_info': academic_info,
        'result': result,
        'total_score': total_score,
        'number_of_course': number_of_course,
        'average_score': average,
        'result_remark': result_remark,
        'general_setting': SchoolGeneralInfoModel.objects.first(),
        'subject_list': subject_list,
        'field_list': field_list,
        'grade_list': grade_list,
        'behaviour_category_list': behaviour_category_list,
        'behaviour_result': behaviour_result,
        'class_minimum': class_minimum,
        'result_type': result_type,
        'midterm_max': midterm_max,

    })
    return render(request, 'student_portal/result/main_result_template.html', context=context)


class ResultSelectView(LoginRequiredMixin, TemplateView):
    template_name = 'student_portal/result/select.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ResultModel = apps.get_model('result', 'ResultModel')
        student = self.request.user.profile.student
        session_list = ResultModel.objects.filter(student=student)
        student_session_list = []
        for session_result in session_list:
            if session_result.session not in student_session_list:
                student_session_list.append(session_result.session)
        context['student_session_list'] = student_session_list
        return context


@login_required
def student_result_archive_sheet_view(request, pk):
    session_pk = request.GET.get('session_pk')
    session = SessionModel.objects.get(pk=session_pk)
    term = request.GET.get('term')
    academic_setting = {
        'term': term,
        'session': session
    }
    student = StudentsModel.objects.get(pk=pk)
    student_class = student.student_class
    class_section = student.class_section
    school_setting = SchoolGeneralInfoModel.objects.first()
    result = ResultModel.objects.filter(term=term, session=session, student=student).first()
    behaviour_category_list = ResultBehaviourCategoryModel.objects.all().order_by('name')
    behaviour_result = ResultBehaviourComputeModel.objects.filter(term=term, session=session,
                                                                  student=student).first()

    if student_class.result_type == 'text':
        if school_setting.separate_school_section:
            result_category_list = TextResultCategoryModel.objects.filter(type=request.user.profile.type).order_by(
                'order')
            result_field_list = TextResultModel.objects.filter(type=request.user.profile.type,
                                                               student_class__in=[student.student_class.id],
                                                               class_section__in=[student.class_section.id]).order_by(
                'name')
        else:
            result_category_list = TextResultCategoryModel.objects.all().order_by('order')
            result_field_list = TextResultModel.objects.filter(student_class__in=[student.student_class.id],
                                                               class_section__in=[student.class_section.id]).order_by(
                'name')

        context = {
            'student': student,
            'result_list': result,
            'academic_setting': academic_setting,
            'behaviour_category_list': behaviour_category_list,
            'behaviour_result': behaviour_result,
            'result_category_list': result_category_list,
            'result_field_list': result_field_list,
            'general_setting': SchoolGeneralInfoModel.objects.first(),
        }
        return render(request, 'result/result/text_result/main_result_template.html', context=context)
		
    result_stat = ResultStatisticModel.objects.filter(term=term, session=session, student_class=student_class,
                                                      class_section=class_section).first()

    result_remark = ResultRemarkModel.objects.filter(term=term, session=session,
                                                     student=student).first()
    total_score = 0
    number_of_course = 0
    average = 0
    total_lowest = 0
    class_minimum = 0
    if result:
        for key, student_result in result.result.items():
            student_result['highest_in_class'] = result_stat.result_statistic[key]['highest_in_class']
            student_result['lowest_in_class'] = result_stat.result_statistic[key]['lowest_in_class']
            total_lowest += result_stat.result_statistic[key]['lowest_in_class']

        number_of_course = len(result.result.items())
        class_minimum = round((total_lowest / (100 * number_of_course)) * 100)
    if result:
        for key, value in result.result.items():
            total_score += value['total']
        average = round((total_score / (100 * number_of_course)) * 100)

    if result:
        for key, student_result in result.result.items():
            student_result['highest_in_class'] = result_stat.result_statistic[key].get('highest_in_class', '')
            student_result['lowest_in_class'] = result_stat.result_statistic[key].get('lowest_in_class', '')
            student_result['average_score'] = result_stat.result_statistic[key].get('average_score', '')
            student_result['midterm_highest_in_class'] = result_stat.result_statistic[key].get('midterm_highest_in_class', '')
            student_result['midterm_lowest_in_class'] = result_stat.result_statistic[key].get('midterm_lowest_in_class', '')
            student_result['midterm_average_score'] = result_stat.result_statistic[key].get('midterm_average_score', '')
            student_result['number_of_student'] = result_stat.result_statistic[key].get('number_of_students', '')
            student_result['has_exam'] = result_stat.result_statistic[key].get('has_exam', '')

    if school_setting.separate_school_section:
        field_list = ResultFieldModel.objects.filter(student_class__in=[student_class]).filter(
                class_section__in=[class_section]).filter(type=request.user.profile.type).order_by('order')
        grade_list = ResultGradeModel.objects.filter(type=request.user.profile.type).order_by('order')
        behaviour_category_list = ResultBehaviourCategoryModel.objects.filter(type=request.user.profile.type).order_by(
            'name')
    else:
        field_list = ResultFieldModel.objects.filter(student_class__in=[student_class]).filter(
                class_section__in=[class_section]).order_by('order')
        grade_list = ResultGradeModel.objects.all().order_by('order')
    if student.subject_group:
        subject_list = student.subject_group.subjects.all()
    else:
        class_detail = ClassSectionInfoModel.objects.filter(student_class=student_class, section=class_section).first()
        if class_detail:
            subject_list = class_detail.subjects
        else:
            subject_list = []

    context = {
        'student': student,
        'academic_setting': academic_setting,
        'result': result,
        'total_score': total_score,
        'number_of_course': number_of_course,
        'average_score': average,
        'result_remark': result_remark,
        'general_setting': SchoolGeneralInfoModel.objects.first(),
        'subject_list': subject_list,
        'field_list': field_list,
        'grade_list': grade_list,
        'behaviour_category_list': behaviour_category_list,
        'behaviour_result': behaviour_result,
        'class_minimum': class_minimum
    }
    return render(request, 'student_portal/result/main_result_template.html', context=context)
