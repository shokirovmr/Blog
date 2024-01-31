from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from shokirov.form import UserRegistrationModelForm, UserLoginForm, PostCreateForm
from shokirov.models import Profile, Post


class HomePageView(View):
    def get(self, request):
        return render(request, 'shokirov/home.html')


class UserRegisterView(View):
    def get(self, request):
        form = UserRegistrationModelForm()
        return render(request, "shokirov/register.html", {"form": form})

    def post(self, request):
        form = UserRegistrationModelForm(data=request.POST)
        if form.is_valid():
            messages.success(request, "User registered successfully")
            form.save()
            return redirect('shokirov:login')
        else:
            return render(request, "shokirov/register.html", {"form": form})


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "shokirov/login.html", {"form": form})

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(request.COOKIES)
                messages.success(request, "User logged in successfully")
                return redirect("shokirov:home-page")
            else:
                messages.error(request, "Username or password is wrong")
                return redirect("shokirov:login")
        else:
            return render(request, "shokirov/login.html", {"form": form})


class UserLogoutView(View):
    def get(self, request):
        return render(request, "shokirov/logout.html")

    def post(self, request):
        logout(request)
        messages.info(request, "User logged out successfully")
        return redirect('shokirov:home-page')


class UserAboutView(View):
    def get(self, request):
        return render(request, "shokirov/about.html")


class UserHomeView(View):
    def get(self, request):
        return render(request, "shokirov/home.html")


class UserPostDetailView(View):
    def get(self, request):
        return render(request, "shokirov/post_detail.html")


class UserPostConfirmDeleteView(View):
    def get(self, request):
        return render(request, "shokirov/post_confirm_delete.html")


class UserPostsView(View):
    def get(self, request):
        return render(request, "shokirov/user_posts.html")


class UserPostsFormView(View):
    def get(self, request):
        return render(request, "shokirov/post_form.html")


class UserPostLarView(View):
    def get(self, request):
        return render(request, "shokirov/user_posts.html")


class UserPostsTuriView(CreateView):
    model = Post
    form = PostCreateForm
    fields = ['title', 'content', 'user']
    template_name = "shokirov/post_form.html"