from django.urls import path
from admin_site.views import *

urlpatterns = [
    path('', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('login', admin_sign_in_view, name='admin_login'),
    path('logout', admin_sign_out_view, name='admin_logout'),

    path('site-info/create', SiteInfoCreateView.as_view(), name='site_info_create'),
    path('site-info/<int:pk>/detail', SiteInfoDetailView.as_view(), name='site_info_detail'),
    path('site-info/<int:pk>/edit', SiteInfoUpdateView.as_view(), name='site_info_edit'),

]

