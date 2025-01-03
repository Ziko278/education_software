from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, CreateView
from admin_dashboard.utility import state_list
from admin_site.forms import ForumQuestionForm, ForumPostForm, SchoolFinderForm
from admin_site.models import SchoolFinderModel, ForumQuestionModel, ForumPostModel, BlogPostModel, BlogCategoryModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class HomePageView(TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state_list'] = state_list
        context['post_list'] = BlogPostModel.objects.all().order_by('-id')[:3]
        return context


class AboutPageView(TemplateView):
    template_name = 'website/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ContactPageView(TemplateView):
    template_name = 'website/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class SchoolFinderPageView(TemplateView):
    template_name = 'website/school_finder.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state_list'] = state_list

        # Filter schools based on user input
        school_list = SchoolFinderModel.objects.filter(status='active')
        keyword = self.request.GET.get('keyword')
        if keyword:
            school_list = school_list.filter(name__icontains=keyword)

        state = self.request.GET.get('state')
        if state:
            school_list = school_list.filter(state=state)

        lga = self.request.GET.get('lga')
        if lga:
            school_list = school_list.filter(lga=lga)

        # Paginate the school list
        paginator = Paginator(school_list, 12)  # 20 schools per page
        page_number = self.request.GET.get('page')
        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            # If page number is not an integer, deliver first page.
            page_obj = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            page_obj = paginator.page(paginator.num_pages)

        context['school_list'] = page_obj
        context['paginator'] = paginator
        return context


class SchoolFinderDetailView(DetailView):
    model = SchoolFinderModel
    template_name = 'website/school_detail.html'
    context_object_name = 'school'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state_list'] = state_list
        return context


class SchoolFinderCreateView(SuccessMessageMixin, CreateView):
    model = SchoolFinderModel
    form_class = SchoolFinderForm
    success_message = 'School Registered, After Confirmation, Your School will be listed'
    template_name = 'website/school_create.html'

    def get_success_url(self):
        return reverse('school_finder_add')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state_list'] = state_list
        return context


class CatalogPageView(TemplateView):
    template_name = 'website/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ResourceCategoryPageView(TemplateView):
    template_name = 'website/resource_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class CalendarExaminationPageView(TemplateView):
    template_name = 'website/calendar/examination.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class CalendarExaminerPageView(TemplateView):
    template_name = 'website/calendar/examiner.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class CalendarStatePageView(TemplateView):
    template_name = 'website/calendar/state.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class StudyAbroadPageView(TemplateView):
    template_name = 'website/study_abroad.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class SchoolManagementPortalPageView(TemplateView):
    template_name = 'website/school_management_portal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


def forum_index_view(request):
    context = {
        'post_list': ForumPostModel.objects.all().order_by('-id')
    }

    return render(request, 'website/forum/index.html', context)


def forum_question_create_view(request):
    if request.method == 'POST':
        form = ForumQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('forum_user_question_index'))
    else:
        form = ForumQuestionForm
    return render(request, 'website/forum/create_question.html', {'form': form})


def forum_user_question_index_view(request):
    context = {
        'question_list': ForumQuestionModel.objects.filter(user=request.user).order_by('-id')
    }
    return render(request, 'website/forum/my_question.html', context)


def forum_question_index_view(request):
    context = {
        'question_list': ForumQuestionModel.objects.all().order_by('-id')
    }
    return render(request, 'website/forum/all_question.html', context)


def forum_post_create_view(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(reverse('forum_post_detail', kwargs={'pk':post.id}))
    else:
        form = ForumPostForm
    return render(request, 'website/forum/create_post.html', {'form': form})


def forum_post_detail_view(request, pk):
    context = {
        'post': get_object_or_404(ForumPostModel, pk=pk)
    }
    return render(request, 'website/forum/post_detail.html', context)


class BlogPageView(TemplateView):
    template_name = 'website/blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_list = BlogPostModel.objects.all().order_by('-id')
        category = self.request.GET.get('category')
        if category:
            post_list = post_list.filter(category__name=category)
        context['post_list'] = post_list
        return context


class BlogDetailPageView(DetailView):
    model = BlogPostModel
    fields = '__all__'
    template_name = 'website/blog/detail.html'
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = BlogCategoryModel.objects.all().order_by('name')
        context['other_blog_list'] = BlogPostModel.objects.filter(category=self.object.category).exclude(pk=self.object.pk).order_by('-created_at')[:5]
        return context


def search_page_view(request):
    category = request.GET.get('category')
    state = request.GET.get('state')
    keyword = request.GET.get('keyword')
    if category == 'school finder':
        return redirect(f"{reverse('school_finder_page')}?keyword={keyword}&state={state}")
    if category == 'blog':
        return redirect(f"{reverse('blog_page')}?keyword={keyword}")
    context = {

    }
    return render(request, 'website/search.html', context)
