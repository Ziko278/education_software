from django.urls import path
from website.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us', AboutPageView.as_view(), name='about_page'),
    path('school-finder', SchoolFinderPageView.as_view(), name='school_finder_page'),
    path('catalog', CatalogPageView.as_view(), name='catalog_page'),
    path('resource-category', ResourceCategoryPageView.as_view(), name='resource_category_page'),
    path('study-abroad', StudyAbroadPageView.as_view(), name='study_abroad_page'),
    path('school-management-portal', SchoolManagementPortalPageView.as_view(), name='school_management_portal_page'),

    path('calendar/examination', CalendarExaminationPageView.as_view(), name='calendar_examination_page'),
    path('calendar/examiner', CalendarExaminerPageView.as_view(), name='calendar_examiner_page'),
    path('calendar/state', CalendarStatePageView.as_view(), name='calendar_state_page'),
]