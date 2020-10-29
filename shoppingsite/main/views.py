from django.shortcuts import render

# Create your views here.


def home(request):

    user = {'is_loggedin': False}

    return render(request, 'main/home.html', {'user': user})


def login(request):
    return render(request, 'main/login.html')


def register(request):

    return render(request, 'main/register.html')


def products(request):
    pass


def cart(request):
    pass


def user(request):
    pass


def logout(request):
    pass
