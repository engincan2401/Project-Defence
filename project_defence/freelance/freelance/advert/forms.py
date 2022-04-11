from freelance.advert.models import Jobs
from django import forms
from freelance.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin


class CreateJobForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        project = super().save(commit=False)

        project.user = self.user
        if commit:
            project.save()

        return project

    class Meta:
        model = Jobs
        fields = ('title', 'type', 'description', 'category', 'budget', 'price')


class EditJobForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Jobs
        exclude = ('user',)
