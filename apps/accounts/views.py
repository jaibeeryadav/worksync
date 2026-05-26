from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .forms import UserRegisterForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from .tokens import account_activation_token

# Create your views here.
class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user)

        email_content = render_to_string(
            "accounts/verification_email.html",
            {
                "user": user,
                "uid": uid,
                "token": token,
            },
        )

        send_mail(
            subject="Verify your WorkSync account",
            message=email_content,
            from_email=None,
            recipient_list=[user.email],
        )

        return redirect("login")

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    next_page = 'dashboard'

class UserLogoutView(LogoutView):
    next_page = "login"

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile
    
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user.profile


from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.shortcuts import redirect

from django.views import View
from .tokens import account_activation_token
from .models import User


class ActivateAccountView(View):

    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)

        except:
            user = None

        if user and account_activation_token.check_token(user, token):
            user.is_active = True
            user.is_verified = True
            user.save()
            return redirect("login")

        return redirect("signup")