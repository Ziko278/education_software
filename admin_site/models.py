from django.db import models


class SiteInfoModel(models.Model):
    name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=50)
    mobile_1 = models.CharField(max_length=20, blank=True, null=True)
    mobile_2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)

    logo = models.FileField(upload_to='images/setting/logo')

    # social media handles
    facebook_handle = models.CharField(max_length=100, null=True, blank=True)
    instagram_handle = models.CharField(max_length=100, null=True, blank=True)
    twitter_handle = models.CharField(max_length=100, null=True, blank=True)
    primary_color = models.CharField(max_length=255)
    secondary_color = models.CharField(max_length=255)

    def __str__(self):
        return self.short_name.upper()




