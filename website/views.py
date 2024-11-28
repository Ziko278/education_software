from django.views.generic import TemplateView


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


class SchoolFinderPageView(TemplateView):
    template_name = 'website/school_finder.html'

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


class SchoolManagementPageView(TemplateView):
    template_name = 'website/school_management.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

