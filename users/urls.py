from django.urls import path

from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, password_recovery

app_name = 'users'
urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/recovery', password_recovery, name='password_recovery'),
]