from django.urls import path
from website.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us', AboutPageView.as_view(), name='about_page'),
    path('contact-us', ContactPageView.as_view(), name='contact_page'),
    path('search', search_page_view, name='search_page'),
    path('school-finder', SchoolFinderPageView.as_view(), name='school_finder_page'),
    path('school-finder/register', SchoolFinderCreateView.as_view(), name='school_finder_add'),
    path('school-finder/<int:pk>/detail', SchoolFinderDetailView.as_view(), name='school_finder_detail_page'),
    path('catalog', CatalogPageView.as_view(), name='catalog_page'),
    path('resource-category', ResourceCategoryPageView.as_view(), name='resource_category_page'),
    path('study-abroad', StudyAbroadPageView.as_view(), name='study_abroad_page'),
    path('school-management-portal', SchoolManagementPortalPageView.as_view(), name='school_management_portal_page'),

    path('calendar/examination', CalendarExaminationPageView.as_view(), name='calendar_examination_page'),
    path('calendar/examiner', CalendarExaminerPageView.as_view(), name='calendar_examiner_page'),
    path('calendar/state', CalendarStatePageView.as_view(), name='calendar_state_page'),

    path('forum/index', forum_index_view, name='forum_index_page'),
    path('forum/ask-question', forum_question_create_view, name='forum_ask_question'),
    path('forum/post', forum_post_create_view, name='forum_create_post'),
    path('forum/post/<int:pk>', forum_post_detail_view, name='forum_post_detail'),
    path('forum/my-questions', forum_user_question_index_view, name='forum_user_question_index'),
    path('forum/questions', forum_question_index_view, name='forum_question_index'),

    path('blog', BlogPageView.as_view(), name='blog_page'),
    path('blog/<int:pk>/detail', BlogDetailPageView.as_view(), name='user_blog_detail'),
]