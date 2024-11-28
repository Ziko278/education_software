from admin_site.models import SiteInfoModel
from django.contrib.auth.models import AnonymousUser, User
from django.shortcuts import redirect


def general_info(request):
    return {
        'site_info': SiteInfoModel.objects.first(),
    }
