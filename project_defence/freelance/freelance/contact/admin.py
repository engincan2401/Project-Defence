from django.contrib import admin

# Register your models here.
from freelance.contact.models import ContactPage, ContactFeedback


class ContactFeedbackAdmin(admin.ModelAdmin):
    list_display = ('your_name', 'email', 'phone_number', 'read')
    readonly_fields = ('your_name', 'email', 'phone_number', 'comment')
    list_filter = ('read',)

    # def has_delete_permission(self, request, obj=None):
    #     return False


admin.site.register(ContactPage)
admin.site.register(ContactFeedback, ContactFeedbackAdmin)
