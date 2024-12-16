from django.urls import path
from student_portal.views import *


urlpatterns = [
    path('my-classmate', StudentClassMateView.as_view(), name='student_classmate'),

    path('dashboard', StudentDashboardView.as_view(), name='student_dashboard'),
    path('result/<int:pk>/current-result', current_term_result, name='student_current_result'),
    path('result-select', ResultSelectView.as_view(), name='student_result_select'),
    path('result/<int:pk>/result-archive/sheet', student_result_archive_sheet_view, name='student_result_archive_sheet'),


]

