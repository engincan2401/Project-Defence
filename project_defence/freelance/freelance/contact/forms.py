from django import forms

from freelance.contact.models import ContactFeedback


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFeedback
        fields = ('your_name', 'email', 'phone_number', 'comment')
