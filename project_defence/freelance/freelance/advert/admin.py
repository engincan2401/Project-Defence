from django.contrib import admin

# Register your models here.
from freelance.advert.models import Categories, Jobs


class JobsAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'created_at', 'user', 'category')
    search_fields = ('title',)

admin.site.register(Categories)
admin.site.register(Jobs, JobsAdmin)
