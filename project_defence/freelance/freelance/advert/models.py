from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.utils.text import slugify
from trans import trans

UserModel = get_user_model()

MAX_LENGTH_TITLE = 50
MAX_LENGTH_DESCRIPTION = 1000

BUDGET_CHOICE = [
    ('1', 'Negotiable'),
    ('2', 'Fixed'),
    ('3', 'Hourly')
]

TYPE_CHOICE = [
    ('1', 'Project'),
    ('2', 'Jobs')
]


class Categories(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, null=True, unique=True, db_index=True, editable=False)

    class Meta:
        verbose_name_plural = 'Advert Categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(trans(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Jobs(models.Model):
    title = models.CharField(max_length=MAX_LENGTH_TITLE)
    type = models.CharField(
        max_length=10,
        default='1',
        choices=TYPE_CHOICE
    )
    description = models.TextField(max_length=MAX_LENGTH_DESCRIPTION)
    created_at = models.DateTimeField(auto_now_add=True)
    budget = models.CharField(
        max_length=10,
        default='1',
        choices=BUDGET_CHOICE
    )
    price = models.FloatField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True, unique=True, db_index=True, editable=False)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Jobs'

    def save(self, *args, **kwargs):
        self.slug = slugify(trans(self.title))
        super().save(*args, **kwargs)
