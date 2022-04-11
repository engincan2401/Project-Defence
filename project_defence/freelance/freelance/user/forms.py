from dal import autocomplete
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser, FreelancerProfile, EmployerProfile, Categories, SubCategories
from ..common.helpers import BootstrapFormMixin


class CustomUserCreationForm(BootstrapFormMixin, UserCreationForm):
    first_name = forms.CharField(
        max_length=FreelancerProfile.FIRST_NAME_MAX_LENGTH,
    )
    last_name = forms.CharField(
        max_length=FreelancerProfile.LAST_NAME_MAX_LENGTH,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        if user.user_choice == '1':
            profile = FreelancerProfile(
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                user=user,
            )
        else:
            profile = EmployerProfile(
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                user=user,
            )

        if commit:
            profile.save()
        return user

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'user_choice')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'user_choice')


# class CreateFreelancerProfileForm(BootstrapFormMixin, forms.ModelForm):
#     category = forms.ModelChoiceField(queryset=Categories.objects.all())
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._init_bootstrap_form_controls()
#
#     def save(self, commit=True):
#         profile = super().save(commit=False)
#
#         profile.user = self.user
#         if commit:
#             profile.save()
#
#         return profile
#
#     class Meta:
#         model = FreelancerProfile
#         fields = ('profile_image', 'hourly_rate', 'description', 'category', 'sub_category')


class EditFreelancerProfileForm(BootstrapFormMixin, forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Categories.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = FreelancerProfile
        fields = ('profile_image', 'first_name', 'last_name', 'hourly_rate', 'description', 'programming_language', 'category', 'sub_category')
        widgets = {
            'sub_category': autocomplete.ListSelect2(url='sub-category-autocomplete',
                                                       forward=['category'])
        }


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return SubCategories.objects.none()

        qs = SubCategories.objects.all()

        category = self.forwarded.get('category', None)

        if category:
            qs = qs.filter(category_id=category)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class EditEmployerProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = EmployerProfile
        fields = ('profile_image', 'first_name', 'last_name', 'description')
