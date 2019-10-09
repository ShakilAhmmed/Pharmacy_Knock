from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    # path('',LoginView.as_view()),password_change
    path('logout',auth_views.LogoutView.as_view(),name="logout"),
    path('',auth_views.LoginView.as_view(template_name="login_panel/login.html",redirect_authenticated_user=True),name="login"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="login_panel/password_reset.html",success_url='done/'), name="password_reset"),
    path('password_change/',auth_views.PasswordChangeView.as_view(success_url='password_change/done/',template_name="login_panel/password_change_form.html"), name="password_change"),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
]
