from django.shortcuts import redirect


class RedirectToHome:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_choice == '1':
                return redirect('home')
        else:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class AuthenticateRedirectToHome:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class RedirectToLogin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            print('g')
            return redirect('user login')
        return super().dispatch(request, *args, **kwargs)
