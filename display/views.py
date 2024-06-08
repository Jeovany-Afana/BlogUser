from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import BlogPost
from .forms import BlogPostForm


# Create your views here.
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirigez vers la page souhaitée après la soumission
    else:
        form = BlogPostForm()
    return render(request, 'create_post.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)  # Utilise 'username' pour l'email

        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials! Please try again.')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    if User.is_authenticated:
        auth.logout(request)

        return redirect('login')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['password2']

        if password == repeat_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered')
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username already registered')
                return redirect('register')

            else:
                user = User.objects.create_user(username.upper(), email, password)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')


def show_posts(request):
    posts = BlogPost.objects.all()
    return render(request, 'index.html', {'posts': posts})


# views.py



