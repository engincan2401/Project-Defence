from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.db import models
from trans import trans
from star_ratings.models import Rating
from freelance.user.managers import CustomUserManager
from django.core.cache import cache
import datetime
from freelance import settings

USER_CHOICE = [
    ('1', 'freelancer'),
    ('2', 'employer')
]


class Categories(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    slug = models.SlugField(blank=True, null=True, unique=True, db_index=True, editable=False)

    class Meta:
        verbose_name_plural = 'Freelancer Categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(trans(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class SubCategories(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True, unique=True, db_index=True, editable=False)

    class Meta:
        verbose_name_plural = 'Freelancer Subcategories'

    def save(self, *args, **kwargs):
        self.slug = slugify(trans(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(_('email address'), unique=True)
    user_choice = models.CharField(max_length=10, default='1', choices=USER_CHOICE)
    last_activity = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class FreelancerProfile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30
    PROGRAMMING_LANGUAGE_MAX_LENGTH = 30

    profile_image = models.ImageField(blank=True, null=True, upload_to='image')
    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH, blank=True, null=True)
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH, blank=True, null=True)
    hourly_rate = models.FloatField(blank=True, null=True)
    programming_language = models.CharField(max_length=PROGRAMMING_LANGUAGE_MAX_LENGTH, blank=True, null=True)

    description = models.TextField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True)
    sub_category = models.ForeignKey(SubCategories, on_delete=models.CASCADE, blank=True, null=True)


class EmployerProfile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    profile_image = models.ImageField(blank=True, null=True, upload_to='image')
    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH, blank=True, null=True)
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH, blank=True, null=True)

    description = models.TextField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
