from django.contrib.auth import views as auth_views
from django.urls import path

from .views import CustomLoginView, CustomLogoutView, RegisterUser

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/reset_password.html'), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_form.html'), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name ='password_reset_complete'),
]
