from django.urls import path

from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, password_recovery, EmailConfirmView, \
    UserConfirmEmailView

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm_register/', EmailConfirmView.as_view(), name='confirm_register'),
    path('confirm-email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/recovery', password_recovery, name='password_recovery'),
]
