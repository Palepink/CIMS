from django.urls import path
from django.contrib.auth import views as auth_view
from .views import index, registerView, UserLoginView

urlpatterns = [
    path('index/', index, name='index'),
    path('register/', registerView, name='register'),
    path('login/', UserLoginView.as_view(template_name='users/login.html'), name='login'),
]
app_name = 'users'
