from django.urls import path, include

from freelance.advert.views import CreateJobsView, DashboardView, JobDetailsView, EditJobView, DeleteJobView

urlpatterns = [
    path('create/', CreateJobsView.as_view(), name='create job'),
    path('jobs/', DashboardView.as_view(), name='jobs'),
    path('job/details/<slug:slug>', JobDetailsView.as_view(), name='job details'),
    path('job/edit/<slug:slug>', EditJobView.as_view(), name='edit job'),
    path('job/delete/<slug:slug>', DeleteJobView.as_view(), name='delete job'),
]
