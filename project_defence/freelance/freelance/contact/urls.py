from django.urls import path

from freelance.contact.views import ContactView

urlpatterns = [
    path('about/', ContactView.as_view(), name='about'),
]