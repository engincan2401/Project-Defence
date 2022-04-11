from django.contrib.auth import views as auth_view
from django.urls import reverse_lazy
from django.views import generic as view
from star_ratings.models import Rating

from freelance.advert.models import Jobs
from freelance.common.view_mixins import AuthenticateRedirectToHome, RedirectToLogin
from freelance.user.forms import EditFreelancerProfileForm, CustomUserCreationForm, \
    EditEmployerProfileForm
from freelance.user.models import FreelancerProfile, CustomUser, EmployerProfile, Categories, SubCategories


class IndexView(view.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ratings = Rating.objects.order_by('-average', '-count')[:5]
        last_viewed = self.request.session.get('last_viewed_freelancer')
        best_freelancer = []
        last_view_freelancer = []
        user_ratings = []

        for rating in ratings:
            if rating.average > 0:
                best_freelancer.append(FreelancerProfile.objects.get(pk=rating.object_id))
                user_ratings.append(rating)

        if last_viewed:
            for last_id in last_viewed:
                last_view_freelancer.append(FreelancerProfile.objects.get(pk=last_id))

        context.update({
            'best_freelancer': best_freelancer,
            'last_view_freelancer': last_view_freelancer,
            'ratings': user_ratings,
        })

        return context


class UserRegisterView(AuthenticateRedirectToHome, view.CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('user login')


class UserLoginView(AuthenticateRedirectToHome, auth_view.LoginView):
    template_name = 'user-login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_view.LogoutView):
    next_page = reverse_lazy('home')


class ProfileDetailsView(RedirectToLogin, view.DetailView):
    model = CustomUser
    template_name = 'profile-details.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        is_owner = self.request.user.pk == self.object.pk
        my_jobs_advert = Jobs.objects.filter(user_id=self.request.user.pk)

        if self.object.user_choice == '1':
            profile = FreelancerProfile.objects.get(user_id=self.object.pk)
        else:
            profile = EmployerProfile.objects.get(user_id=self.object.pk)

        context.update({
            'profile': profile,
            'is_owner': is_owner,
            'jobs': my_jobs_advert,
        })

        if self.object.pk != self.request.user.pk and self.object.user_choice == '1':
            last_viewed = self.request.session.get('last_viewed_freelancer') or []

            if self.object.pk not in last_viewed:
                last_viewed.append(self.object.pk)
                self.request.session['last_viewed_freelancer'] = last_viewed

        return context


# class CreateProfileView(RedirectToEditProfile, view.CreateView):
#     template_name = 'create-profile.html'
#     form_class = CreateFreelancerProfileForm
#     success_url = reverse_lazy('home')
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['user'] = self.request.user
#         return kwargs


class EditFreelancerProfileView(view.UpdateView):
    template_name = 'edit-freelancer-profile.html'
    form_class = EditFreelancerProfileForm
    model = FreelancerProfile
    success_url = reverse_lazy('home')


class EditEmployerProfileView(view.UpdateView):
    template_name = 'edit-employer-profile.html'
    form_class = EditEmployerProfileForm
    model = EmployerProfile
    success_url = reverse_lazy('home')


class ListFreelancerView(RedirectToLogin, view.ListView):
    model = FreelancerProfile
    template_name = 'list-freelancer.html'

    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get('search')

        if search:
            queryset = FreelancerProfile.objects.filter(
                programming_language__contains=search) or FreelancerProfile.objects.filter(
                description__contains=search) or FreelancerProfile.objects.filter(
                category__title__contains=search) or FreelancerProfile.objects.filter(
                sub_category__title__contains=search)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Categories.objects.all()
        ratings = Rating.objects.all()
        last_viewed = self.request.session.get('last_viewed_freelancer')
        last_view_freelancer = []
        user_ratings = []

        for rating in ratings:
            if rating.average > 0:
                user_ratings.append(rating)

        if last_viewed:
            for last_id in last_viewed:
                last_view_freelancer.append(FreelancerProfile.objects.get(pk=last_id))

        context.update({
            'categories': categories,
            'ratings': user_ratings,
            'last_view_freelancer': last_view_freelancer,
        })

        return context


class ListFreelancerWithCategoryView(RedirectToLogin, view.ListView):
    model = FreelancerProfile
    template_name = 'list-freelancer-with-category.html'

    def get_queryset(self):
        id = self.kwargs['id']
        qs = self.request.GET.get('filter')
        search = self.request.GET.get('search')

        queryset = FreelancerProfile.objects.filter(category_id=id)
        if qs:
            queryset = FreelancerProfile.objects.filter(category_id=id).filter(sub_category_id=qs)

        if search:
            queryset = FreelancerProfile.objects.filter(
                programming_language__contains=search) or FreelancerProfile.objects.filter(
                description__contains=search)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['id']
        sub_category = SubCategories.objects.filter(category_id=id)
        category_name = Categories.objects.get(pk=id).title
        ratings = Rating.objects.all()
        user_ratings = []

        for rating in ratings:
            if rating.average > 0:
                user_ratings.append(rating)

        context.update({
            'sub_category': sub_category,
            'category_name': category_name,
            'ratings': user_ratings,
        })

        return context
