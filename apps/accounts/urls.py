from django.urls import URLPattern
from.views import UserLoginView, UserLogoutView, UserRegisterView, ProfileUpdateView, ProfileDetailView, ActivateAccountView
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path("password-reset/",auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html",
                                                                email_template_name="registration/password_reset_email.html",),name="password_reset",),

    path("password-reset/done/",auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"),name="password_reset_done",),

    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"),name="password_reset_confirm",),

    path("reset/done/",auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"),name="password_reset_complete",),
    path("activate/<uidb64>/<token>/",ActivateAccountView.as_view(),name="activate",),
] 
