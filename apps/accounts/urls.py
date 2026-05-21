from django.urls import URLPattern
from.views import UserLoginView, UserLogoutView, UserRegisterView
from django.urls import path
urlpatterns = [
    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
