from django.shortcuts import render, HttpResponse, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm, LoginForm
from .models import UserProfile


def index(request):
    return render(request, 'index.html')


def registerView(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.save(commit=True)
            return HttpResponse('successful')
        return render(request, 'users/register.html', locals())
    if request.method == 'GET':
        register_form = RegisterForm
        return render(request, 'users/register.html', locals())


class UserLoginView(LoginView):
    form_class = LoginForm

    def get_success_url(self):
        return reverse('index', )
