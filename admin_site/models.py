from django.contrib.auth.models import User
from django.db import models
from slugify import slugify


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


class SchoolAmenityModel(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name.upper()


class SchoolTypeModel(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name.upper()


class SchoolFinderModel(models.Model):
    name = models.CharField(max_length=250)
    school_type = models.ManyToManyField(SchoolTypeModel, blank=True)
    BOARDING_TYPE = (('day', 'DAY'), ('boarding', 'BOARDING'), ('combined', 'COMBINED'))
    boarding_type = models.CharField(max_length=50, choices=BOARDING_TYPE, blank=True, null=True)
    GENDER = (('male', 'MALE'), ('female', 'FEMALE'), ('combined', 'COMBINED'))
    gender = models.CharField(max_length=50, choices=GENDER, blank=True, null=True)
    mobile_1 = models.CharField(max_length=20, blank=True, null=True)
    mobile_2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    lga = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    logo = models.FileField(upload_to='images/setting/logo')
    short_description = models.TextField(blank=True, null=True)
    main_description = models.TextField(blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    amenities = models.ManyToManyField(SchoolAmenityModel, blank=True)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    school_owner_name = models.CharField(max_length=200, blank=True, null=True)
    school_head_name = models.CharField(max_length=200, blank=True, null=True)
    registrar_name = models.CharField(max_length=200, blank=True, null=True)
    registrar_position = models.CharField(max_length=100, blank=True, null=True)
    registrar_mobile = models.CharField(max_length=100, blank=True, null=True)
    STATUS = (
        ('active', 'ACTIVE'), ('pending', 'PENDING')
    )
    status = models.CharField(max_length=20, choices=STATUS, blank=True, default='pending')

    def __str__(self):
        return self.name.upper()


class ForumTagModel(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name.upper()


class ForumQuestionModel(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    PRIVACY = (('public', 'PUBLIC'), ('private', 'PRIVATE'))
    privacy = models.CharField(max_length=20, blank=True, default='public')
    upvote = models.IntegerField(blank=True, default=0)
    downvote = models.IntegerField(blank=True, default=0)
    vote = models.IntegerField(blank=True, default=0)
    upvoters = models.JSONField(default={}, blank=True)
    downvoters = models.JSONField(default={}, blank=True)
    STATUS = (
        ('active', 'ACTIVE'), ('pending', 'PENDING')
    )
    status = models.CharField(max_length=20, choices=STATUS, blank=True, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title.upper()


class ForumAnswerModel(models.Model):
    question = models.ForeignKey(ForumQuestionModel, on_delete=models.CASCADE)
    answer = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    privacy = models.BooleanField(blank=True, default=False)
    upvote = models.IntegerField(blank=True, default=0)
    downvote = models.IntegerField(blank=True, default=0)
    vote = models.IntegerField(blank=True, default=0)
    upvoters = models.JSONField(default={}, blank=True)
    downvoters = models.JSONField(default={}, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS = (
        ('active', 'ACTIVE'), ('pending', 'PENDING')
    )
    status = models.CharField(max_length=20, choices=STATUS, blank=True, default='pending')

    def __str__(self):
        return self.answer


class ForumPostModel(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/forum')
    description = models.TextField()
    detail = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    privacy = models.BooleanField(blank=True, default=False)
    upvote = models.IntegerField(blank=True, default=0)
    downvote = models.IntegerField(blank=True, default=0)
    vote = models.IntegerField(blank=True, default=0)
    upvoters = models.JSONField(default={}, blank=True)
    downvoters = models.JSONField(default={}, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS = (
        ('active', 'ACTIVE'), ('pending', 'PENDING')
    )
    status = models.CharField(max_length=20, choices=STATUS, blank=True, default='pending')

    def __str__(self):
        return self.title


class ForumCommentModel(models.Model):
    answer = models.TextField()
    image = models.ImageField(upload_to='images/forum')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    privacy = models.BooleanField(blank=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS = (
        ('active', 'ACTIVE'), ('pending', 'PENDING')
    )
    status = models.CharField(max_length=20, choices=STATUS, blank=True, default='pending')

    def __str__(self):
        return self.answer


class BlogCategoryModel(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name.upper()

    def no_of_post(self):
        return BlogPostModel.objects.filter(category=self).count()


class BlogTagModel(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name.upper()


class BlogPostModel(models.Model):
    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=250)
    category = models.ForeignKey(BlogCategoryModel, on_delete=models.CASCADE)
    tag = models.ManyToManyField(BlogTagModel, blank=True)
    description = models.TextField()
    image = models.FileField(upload_to='images/blog/post')
    blog_detail = models.TextField()
    no_of_views = models.IntegerField(blank=True, default=0)
    STATUS = (('active', 'ACTIVE'), ('inactive', 'INACTIVE'))
    status = models.CharField(max_length=20, choices=STATUS, default='active')
    key = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title.upper()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.key = str(self.title) + str(self.category.name)
        super(BlogPostModel, self).save(*args, **kwargs)


class BlogCommentModel(models.Model):
    post = models.ForeignKey(BlogPostModel, related_name='comment', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    comments = models.TextField()
    STATUS = (('active', 'ACTIVE'), ('inactive', 'INACTIVE'))
    status = models.CharField(max_length=20, choices=STATUS, default='active', blank=True)


class BlogResponseModel(models.Model):
    comment = models.ForeignKey(BlogCommentModel, on_delete=models.CASCADE)
    response = models.TextField()
    STATUS = (('active', 'ACTIVE'), ('inactive', 'INACTIVE'))
    status = models.CharField(max_length=20, choices=STATUS, default='active')
