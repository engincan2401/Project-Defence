from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models

# Create your models here.


class ContactPage(models.Model):
    TITLE_MAX_LENGTH = 30
    CONTENT_MAX_LENGTH = 500

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'Contact Page Content'

    def __str__(self):
        return self.title


class ContactFeedback(models.Model):
    NAME_MAX_LENGTH = 30
    COMMENT_MAX_LENGTH = 500

    your_name = models.CharField(max_length=NAME_MAX_LENGTH)
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        validators=[MinLengthValidator(9), MaxLengthValidator(9)]
    )
    comment = models.TextField(validators=[MaxLengthValidator(COMMENT_MAX_LENGTH)])
    read = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return self.your_name
