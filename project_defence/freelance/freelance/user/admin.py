from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Categories, SubCategories, FreelancerProfile, EmployerProfile


name = 'FreelancerBG administration'
admin.site.site_title = name
admin.site.site_header = name
admin.site.index_title = name


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'user_choice', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions',)
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_choice', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class FreelancerProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'programming_language')
    ordering = ('first_name',)


class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)
    ordering = ('first_name',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(FreelancerProfile, FreelancerProfileAdmin)
admin.site.register(EmployerProfile, EmployerProfileAdmin)
