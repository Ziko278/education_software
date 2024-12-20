from django.urls import path
from admin_site.views import *

urlpatterns = [
    path('', AdminDashboardView.as_view(), name='site_dashboard'),
    path('login', admin_sign_in_view, name='admin_login'),
    path('logout', admin_sign_out_view, name='admin_logout'),

    path('site-info/create', SiteInfoCreateView.as_view(), name='site_info_create'),
    path('site-info/<int:pk>/detail', SiteInfoDetailView.as_view(), name='site_info_detail'),
    path('site-info/<int:pk>/edit', SiteInfoUpdateView.as_view(), name='site_info_edit'),

    path('school/amenity/create', SchoolAmenityCreateView.as_view(), name='school_amenity_create'),
    path('school/amenity/index', SchoolAmenityListView.as_view(), name='school_amenity_index'),
    path('school/amenity/<int:pk>/edit', SchoolAmenityUpdateView.as_view(), name='school_amenity_edit'),
    path('school/amenity/<int:pk>/delete', SchoolAmenityDeleteView.as_view(), name='school_amenity_delete'),

    path('school/finder/create', SchoolFinderCreateView.as_view(), name='school_finder_create'),
    path('school/finder/index', SchoolFinderListView.as_view(), name='school_finder_index'),
    path('school/finder/<int:pk>/detail', SchoolFinderDetailView.as_view(), name='school_finder_detail'),
    path('school/finder/<int:pk>/approve', school_finder_approve_view, name='school_finder_approve'),
    path('school/finder/<int:pk>/edit', SchoolFinderUpdateView.as_view(), name='school_finder_edit'),
    path('school/finder/<int:pk>/delete', SchoolFinderDeleteView.as_view(), name='school_finder_delete'),

    path('blog/category/register', BlogCategoryCreateView.as_view(), name='blog_category_create'),
    path('blog/category/index', BlogCategoryListView.as_view(), name='blog_category_index'),
    path('blog/category/<int:pk>/edit', BlogCategoryUpdateView.as_view(), name='blog_category_edit'),
    path('blog/category/<int:pk>/delete', BlogCategoryDeleteView.as_view(), name='blog_category_delete'),

    path('blog/tag/register', BlogTagCreateView.as_view(), name='blog_tag_create'),
    path('blog/tag/index', BlogTagListView.as_view(), name='blog_tag_index'),
    path('blog/tag/<int:pk>/edit', BlogTagUpdateView.as_view(), name='blog_tag_edit'),
    path('blog/tag/<int:pk>/delete', BlogTagDeleteView.as_view(), name='blog_tag_delete'),

    path('blog/post/register', BlogPostCreateView.as_view(), name='blog_post_create'),
    path('blog/post/index', BlogPostListView.as_view(), name='blog_post_index'),
    path('blog/post/<int:pk>/edit', BlogPostUpdateView.as_view(), name='blog_post_edit'),
    path('blog/post/<int:pk>/detail', BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('blog/post/<int:pk>/delete', BlogPostDeleteView.as_view(), name='blog_post_delete'),

    path('blog/post/comment/register', BlogCommentCreateView.as_view(), name='blog_comment_create'),
    path('blog/post/comment/index', BlogCommentListView.as_view(), name='blog_comment_index'),
    path('blog/post/comment/<int:pk>/edit', BlogCommentUpdateView.as_view(), name='blog_comment_edit'),
    path('blog/post/comment/<int:pk>/detail', BlogCommentDetailView.as_view(), name='blog_comment_detail'),
    path('blog/post/comment/<int:pk>/delete', BlogCommentDeleteView.as_view(), name='blog_comment_delete'),

]

