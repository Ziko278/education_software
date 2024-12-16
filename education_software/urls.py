from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('website.urls')),
    path('admin/', include('admin_site.urls')),

    path('school-portal/admin/', include('admin_dashboard.urls')),
    path('school-portal/student/', include('student.urls')),
    path('school-portal/communication/', include('communication.urls')),
    path('school-portal/result/', include('result.urls')),
    path('school-portal/student-portal/', include('student_portal.urls')),
    path('school-portal/setting/', include('school_setting.urls')),
    path('school-portal/site/', include('user_management.urls')),
    path('school-portal/human_resource/', include('human_resource.urls')),
    path('school-portal/academic/', include('academic.urls')),
    path('django-admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


