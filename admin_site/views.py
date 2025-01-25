import json
import random

import pytz
import requests
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from admin_site.forms import SiteInfoForm, SchoolAmenityForm, SchoolFinderForm, BlogResponseForm, BlogCommentForm, \
    BlogPostForm, BlogTagForm, BlogCategoryForm
from admin_site.models import SiteInfoModel, SchoolAmenityModel, SchoolFinderModel, BlogResponseModel, BlogCommentModel, \
    BlogPostModel, BlogTagModel, BlogCategoryModel

from datetime import date, datetime, timedelta
from django.utils import timezone

from django.db import transaction


class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'admin_site/dashboard.html'

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(reverse('admin_login'))
        return super(AdminDashboardView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class SiteInfoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = SiteInfoModel
    form_class = SiteInfoForm
    permission_required = 'admin_site.change_siteinfomodel'
    success_message = 'Site Information Updated Successfully'
    template_name = 'admin_site/site_info/create.html'

    def dispatch(self, *args, **kwargs):
        site_info = SiteInfoModel.objects.first()
        if not site_info:
            return super(SiteInfoCreateView, self).dispatch(*args, **kwargs)
        else:
            return redirect(reverse('site_info_edit', kwargs={'pk': site_info.pk}))

    def get_success_url(self):
        return reverse('site_info_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SiteInfoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = SiteInfoModel
    permission_required = 'admin_site.view_siteinfomodel'
    fields = '__all__'
    template_name = 'admin_site/site_info/detail.html'
    context_object_name = "site_info"

    def dispatch(self, *args, **kwargs):
        site_info = SiteInfoModel.objects.first()
        if site_info:
            if self.kwargs.get('pk') != site_info.id:
                return redirect(reverse('site_info_detail', kwargs={'pk': site_info.pk}))
            return super(SiteInfoDetailView, self).dispatch(*args, **kwargs)
        else:
            return redirect(reverse('site_info_create'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class SiteInfoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SiteInfoModel
    permission_required = 'admin_site.change_siteinfomodel'
    form_class = SiteInfoForm
    success_message = 'Site Information Updated Successfully'
    template_name = 'admin_site/site_info/create.html'

    def get_success_url(self):
        return reverse('site_info_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_info'] = self.object
        return context


def admin_sign_in_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            intended_route = request.POST.get('next') or request.GET.get('next')
            remember_me = request.POST.get('remember_me') or request.GET.get('remember_me')

            if user.is_superuser:
                login(request, user)
                messages.success(request, 'welcome back {}'.format(user.username.title()))
                if remember_me:
                    request.session.set_expiry(3600 * 24 * 30)
                else:
                    request.session.set_expiry(0)
                if intended_route:
                    return redirect(intended_route)
                return redirect(reverse('site_dashboard'))

            else:
                messages.error(request, 'Unknown Identity, Access Denied')
                return redirect(reverse('login'))
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect(reverse('admin_login'))

    return render(request, 'admin_site/sign_in.html')


def admin_sign_out_view(request):
    logout(request)
    return redirect(reverse('admin_login'))


class SchoolAmenityCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = SchoolAmenityModel
    permission_required = 'school.add_schoolamenitymodel'
    form_class = SchoolAmenityForm
    success_message = 'School Amenity Added Successfully'
    template_name = 'admin_site/school_amenity/index.html'

    def get_success_url(self):
        return reverse('school_amenity_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['school_amenity_list'] = SchoolAmenityModel.objects.all().order_by('name')
        return context


class SchoolAmenityListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = SchoolAmenityModel
    permission_required = 'school.view_schoolamenitymodel'
    fields = '__all__'
    template_name = 'admin_site/school_amenity/index.html'
    context_object_name = "school_amenity_list"

    def get_queryset(self):
        return SchoolAmenityModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SchoolAmenityForm

        return context


class SchoolAmenityUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SchoolAmenityModel
    permission_required = 'school.change_schoolamenitymodel'
    form_class = SchoolAmenityForm
    success_message = 'School Amenity Updated Successfully'
    template_name = 'admin_site/school_amenity/index.html'

    def get_success_url(self):
        return reverse('school_amenity_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school_amenity_list'] = SchoolAmenityModel.objects.all().order_by('name')
        context['form'] = SchoolAmenityForm
        return context


class SchoolAmenityDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = SchoolAmenityModel
    permission_required = 'school.delete_schoolamenitymodel'
    success_message = 'School Amenity Deleted Successfully'
    fields = '__all__'
    template_name = 'admin_site/school_amenity/delete.html'
    context_object_name = "school_amenity"

    def get_success_url(self):
        return reverse("school_amenity_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SchoolFinderCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = SchoolFinderModel
    permission_required = 'school.add_schoolfindermodel'
    form_class = SchoolFinderForm
    success_message = 'School Finder Added Successfully'
    template_name = 'admin_site/school_finder/create.html'

    def get_success_url(self):
        return reverse('school_finder_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SchoolFinderListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = SchoolFinderModel
    permission_required = 'school.view_schoolfindermodel'
    fields = '__all__'
    template_name = 'admin_site/school_finder/index.html'
    context_object_name = "school_list"

    def get_queryset(self):
        return SchoolFinderModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class SchoolFinderDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = SchoolFinderModel
    permission_required = 'human_resource.view_staffmodel'
    fields = '__all__'
    template_name = 'admin_site/school_finder/detail.html'
    context_object_name = "school"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class SchoolFinderUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SchoolFinderModel
    permission_required = 'school.change_schoolfindermodel'
    form_class = SchoolFinderForm
    success_message = 'School Finder Updated Successfully'
    template_name = 'admin_site/school_finder/edit.html'

    def get_success_url(self):
        return reverse('school_finder_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school'] = self.object
        return context


@login_required
def school_finder_approve_view(request, pk):
    if request.method == 'POST':
        school = SchoolFinderModel.objects.get(pk=pk)
        school.status = 'active'

        school.save()
        messages.success(request, 'School Approved and Listed')

    return redirect(reverse('school_finder_detail', kwargs={'pk': pk}))


class SchoolFinderDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = SchoolFinderModel
    permission_required = 'school.delete_schoolfindermodel'
    success_message = 'School Finder Deleted Successfully'
    fields = '__all__'
    template_name = 'admin_site/school_finder/delete.html'
    context_object_name = "school_finder"

    def get_success_url(self):
        return reverse("school_finder_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogCategoryCreateView(SuccessMessageMixin, CreateView):
    model = BlogCategoryModel
    form_class = BlogCategoryForm
    template_name = 'blog_category/index.html'
    success_message = 'Blog Category Added Successfully'

    def get_success_url(self):
        return reverse('blog_category_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogCategoryListView(ListView):
    model = BlogCategoryModel
    fields = '__all__'
    template_name = 'admin_site/blog_category/index.html'
    context_object_name = "category_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogCategoryForm
        return context


class BlogCategoryUpdateView(SuccessMessageMixin, UpdateView):
    model = BlogCategoryModel
    form_class = BlogCategoryForm
    template_name = 'admin_site/blog_category/index.html'
    success_message = 'Blog Category Successfully Updated'

    def get_success_url(self):
        return reverse('blog_category_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogCategoryDeleteView(DeleteView):
    model = BlogCategoryModel
    template_name = 'admin_site/blog_category/delete.html'
    context_object_name = "category"

    def get_success_url(self):
        return reverse('blog_category_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogTagCreateView(SuccessMessageMixin, CreateView):
    model = BlogTagModel
    form_class = BlogTagForm
    template_name = 'admin_site/blog_tag_create.html'
    success_message = 'Blog Tag Added Successfully'

    def get_success_url(self):
        return reverse('blog_tag_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogTagListView(ListView):
    model = BlogTagModel
    fields = '__all__'
    template_name = 'admin_site/blog_tag/index.html'
    context_object_name = "tag_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogTagForm
        return context


class BlogTagUpdateView(SuccessMessageMixin, UpdateView):
    model = BlogTagModel
    form_class = BlogTagForm
    template_name = 'admin_site/blog_tag/edit.html'
    success_message = 'Blog Tag Successfully Updated'

    def get_success_url(self):
        return reverse('blog_tag_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogTagDeleteView(DeleteView):
    model = BlogTagModel
    template_name = 'admin_site/blog_tag/delete.html'
    context_object_name = "tag"

    def get_success_url(self):
        return reverse('blog_tag_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogPostCreateView(SuccessMessageMixin, CreateView):
    model = BlogPostModel
    form_class = BlogPostForm
    template_name = 'admin_site/blog_post/create.html'
    success_message = 'Blog Post Added Successfully'

    def get_success_url(self):
        return reverse('blog_post_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_list'] = BlogTagModel.objects.all().order_by('name')

        return context


class BlogPostListView(ListView):
    model = BlogPostModel
    fields = '__all__'
    template_name = 'admin_site/blog_post/index.html'
    context_object_name = "post_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogPostForm
        return context


class BlogPostDetailView(LoginRequiredMixin, DetailView):
    model = BlogPostModel
    fields = '__all__'
    template_name = 'admin_site/blog_post/detail.html'
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogPostUpdateView(SuccessMessageMixin, UpdateView):
    model = BlogPostModel
    form_class = BlogPostForm
    template_name = 'admin_site/blog_post/edit.html'
    success_message = 'Blog Post Successfully Updated'

    def get_success_url(self):
        return reverse('blog_post_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_list'] = BlogTagModel.objects.all().order_by('name')
        context['post'] = self.object
        return context


class BlogPostDeleteView(DeleteView):
    model = BlogPostModel
    template_name = 'admin_site/blog_post/delete.html'
    context_object_name = "blog_post"

    def get_success_url(self):
        return reverse('blog_post_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogCommentCreateView(SuccessMessageMixin, CreateView):
    model = BlogCommentModel
    form_class = BlogCommentForm
    template_name = 'admin_site/blog_comment/index.html'
    success_message = 'Comment Added Successfully'

    def get_success_url(self):
        return reverse('blog_detail', kwargs={'slug': self.object.post.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogCommentListView(ListView):
    model = BlogCommentModel
    fields = '__all__'
    template_name = 'admin_site/blog_comment/index.html'
    context_object_name = "comment_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogCommentForm
        return context


class BlogCommentDetailView(LoginRequiredMixin, DetailView):
    model = BlogCommentModel
    fields = '__all__'
    template_name = 'admin_site/blog_comment/detail.html'
    context_object_name = "comment"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogCommentUpdateView(SuccessMessageMixin, UpdateView):
    model = BlogCommentModel
    form_class = BlogCommentForm
    template_name = 'admin_site/blog_comment/edit.html'
    success_message = 'Comment Successfully Updated'

    def get_success_url(self):
        return reverse('blog_comment_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogCommentDeleteView(DeleteView):
    model = BlogCommentModel
    template_name = 'admin_site/blog_comment/delete.html'
    context_object_name = "comment"

    def get_success_url(self):
        return reverse('blog_comment_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogResponseCreateView(SuccessMessageMixin, CreateView):
    model = BlogResponseModel
    form_class = BlogResponseForm
    template_name = 'admin_site/blog_response/index.html'
    success_message = 'Response Added Successfully'

    def get_success_url(self):
        return reverse('blog_response_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogResponseListView(ListView):
    model = BlogResponseModel
    fields = '__all__'
    template_name = 'admin_site/blog_response/index.html'
    context_object_name = "response_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogResponseForm()
        return context


class BlogResponseDetailView(LoginRequiredMixin, DetailView):
    model = BlogResponseModel
    fields = '__all__'
    template_name = 'admin_site/blog_response/detail.html'
    context_object_name = "response"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogResponseUpdateView(SuccessMessageMixin, UpdateView):
    model = BlogResponseModel
    form_class = BlogResponseForm
    template_name = 'admin_site/blog_response/index.html'
    success_message = 'Response Successfully Updated'

    def get_success_url(self):
        return reverse('blog_response_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogResponseDeleteView(DeleteView):
    model = BlogResponseModel
    template_name = 'admin_site/blog_response/delete.html'
    context_object_name = "response"

    def get_success_url(self):
        return reverse('blog_response_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
