from django.urls import path

from freelance.user.forms import CategoryAutocomplete
from freelance.user.views import ProfileDetailsView, UserLoginView, EditFreelancerProfileView, \
    UserRegisterView, UserLogoutView, EditEmployerProfileView, ListFreelancerView, ListFreelancerWithCategoryView

urlpatterns = [
    path('profile/<int:pk>', ProfileDetailsView.as_view(), name='profile details'),
    path('login/', UserLoginView.as_view(), name='user login'),
    path('register/', UserRegisterView.as_view(), name='user register'),
    path('logout/', UserLogoutView.as_view(), name='user logout'),
    path('edit-freelancer-profile/<int:pk>', EditFreelancerProfileView.as_view(), name='edit freelancer profile'),
    path('edit-employer-profile/<int:pk>', EditEmployerProfileView.as_view(), name='edit employer profile'),
    path('sub-category-autocomplete/', CategoryAutocomplete.as_view(), name='sub-category-autocomplete'),
    path('freelancer-list/', ListFreelancerView.as_view(), name='freelancer'),
    path('freelancer/category/<int:id>', ListFreelancerWithCategoryView.as_view(), name='freelancer with category'),
]
