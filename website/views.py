import json

from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, CreateView
from admin_site.forms import ForumQuestionForm, ForumPostForm, SchoolFinderForm
from admin_site.models import SchoolFinderModel, ForumQuestionModel, ForumPostModel, BlogPostModel, BlogCategoryModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class HomePageView(TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
        return context


class SchoolFinderDetailView(DetailView):
    model = SchoolFinderModel
    template_name = 'website/school_detail.html'
    context_object_name = 'school'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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


class StudyAbroadPlacementPageView(TemplateView):
    template_name = 'website/study_abroad_placement.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class StudyAbroadWorkFlowPageView(TemplateView):
    template_name = 'website/study_abroad_workflow.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class SchoolManagementPortalPageView(TemplateView):
    template_name = 'website/school_management_portal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class TrainingAndWorkshopPageView(TemplateView):
    template_name = 'website/training_and_workshop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    
    
class ProcessAutomationPageView(TemplateView):
    template_name = 'website/process_automation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ExcursionPageView(TemplateView):
    template_name = 'website/excursion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class SolarDetailPageView(TemplateView):
    template_name = 'website/detail/solar.html'

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


def send_update_mail(request):
    if request.method == 'GET':
        # Retrieve the raw data (sent as 'updated_data' in the request)
        updated_data = request.GET.get('updated_data', None)

        if updated_data:
            try:
                # Parse the JSON string into a Python dictionary
                data = json.loads(updated_data)

                # Construct the email body in 'key: Value' format
                school_name = ''
                message = ""
                for key, value in data.items():
                    if key == 'school_namecd':
                        school_name = key.upper()
                    message += f"{key}: {value}\n"  # Format the message

                # Prepare the email details
                subject = f'UPDATED SCHOOL DATA FOR {school_name}'
                from_email = 'odekeziko@gmail.com'
                recipient_list = ['contact@braintree.com.ng', 'braintreeresources@gmail.com']  # List of email addresses

                # Send the email
                send_mail(subject, message, from_email, recipient_list)

                # Return a success response
                return JsonResponse({'status': 'success', 'message': 'Email sent successfully'})
            except json.JSONDecodeError:
                return JsonResponse({'status': 'fail', 'message': 'Failed to decode JSON data'}, status=400)
        else:
            return JsonResponse({'status': 'fail', 'message': 'No data received'}, status=400)

    return JsonResponse({'status': 'fail', 'message': 'Invalid request method'}, status=400)


def send_quotation_email(request):
    if request.method == "GET":
        try:
            # Prepare the message body dynamically
            message = "A new quotation request has been received:\n\n"

            # Iterate through all GET parameters and add them to the message
            for key, value in request.GET.items():
                # Format the field names and values into the message
                field_name = key.replace("-", " ").title()  # Convert keys to a more readable format
                field_value = value
                message += f"{field_name}: {field_value}\n"

            subject = "New Quotation Request"
            from_email = 'odekeziko@gmail.com'
            recipient_list = ['contact@braintree.com.ng', 'braintreeresources@gmail.com']  # List of email addresses

            # Send the email
            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,
            )

            return JsonResponse({"success": True, "message": "Quotation sent successfully!"})

        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)}, status=400)

    return JsonResponse({"success": False, "message": "Invalid request"}, status=400)

