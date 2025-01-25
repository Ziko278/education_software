from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('website.urls')),
    path('admin/', include('admin_site.urls')),

    path('sch-portal/', include('admin_dashboard.urls')),
    path('sch-portal/student/', include('student.urls')),
    path('sch-portal/communication/', include('communication.urls')),
    path('sch-portal/result/', include('result.urls')),
    path('sch-portal/student-portal/', include('student_portal.urls')),
    path('sch-portal/setting/', include('school_setting.urls')),
    path('sch-portal/site/', include('user_management.urls')),
    path('sch-portal/human_resource/', include('human_resource.urls')),
    path('sch-portal/academic/', include('academic.urls')),
    path('sch-portal/attendance/', include('attendance.urls')),
    path('sch-portal/finance/', include('finance.urls')),

    path('django-admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


