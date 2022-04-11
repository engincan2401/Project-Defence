from django.shortcuts import redirect
from django.views import generic as view

from freelance.contact.forms import ContactForm
from freelance.contact.models import ContactPage


class ContactView(view.TemplateView):
    template_name = 'contact-page.html'

    def post(self, *args, **kwargs):
        form = ContactForm(self.request.POST)
        print(form)
        print(form.errors)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.phone_number = '0' + feedback.phone_number
            feedback.save()
            return redirect('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = ContactPage.objects.first()
        form = ContactForm()

        context.update({
            'object': object,
            'form': form
        })

        return context
