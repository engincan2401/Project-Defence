from django.urls import reverse_lazy
from django.views import generic as view
from freelance.advert.forms import CreateJobForm, EditJobForm
from freelance.advert.models import Jobs, Categories
from freelance.common.view_mixins import RedirectToHome, RedirectToLogin


class CreateJobsView(RedirectToHome, view.CreateView):
    template_name = 'create-job.html'
    form_class = CreateJobForm
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class DashboardView(RedirectToLogin, view.ListView):
    model = Jobs
    template_name = 'jobs-list.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        queryset = super().get_queryset()
        qs = self.request.GET.get('filter')
        search = self.request.GET.get('search')

        if qs:
            queryset = queryset.filter(category_id=qs)

        if search:
            queryset = Jobs.objects.filter(title__contains=search) or Jobs.objects.filter(description__contains=search)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        categories = Categories.objects.all()

        context.update({
            'categories': categories
        })

        return context


class JobDetailsView(RedirectToLogin, view.DetailView):
    model = Jobs
    template_name = 'jobs-details.html'
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        is_owner = self.request.user.pk == self.object.user.pk

        context.update({
            'is_owner': is_owner
        })

        return context


class EditJobView(RedirectToHome, view.UpdateView):
    template_name = 'edit-job.html'
    form_class = EditJobForm
    model = Jobs
    success_url = reverse_lazy('home')


class DeleteJobView(RedirectToHome, view.DeleteView):
    template_name = 'delete-job.html'
    model = Jobs
    success_url = reverse_lazy('home')
