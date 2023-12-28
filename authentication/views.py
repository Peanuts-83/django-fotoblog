import string
from django.forms import Form
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms

from fotoblog import settings
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View


class AuthView(View):
    form_class: Form = forms.BaseForm
    template_name: string = ""
    message = ""

    def get(self, request) -> HttpResponse:
        form = self.form_class()
        if len(self.template_name) > 0:
            # user is logged > redirect to home
            if request.user.is_authenticated:
                return redirect('home')
            # else allow signin process
            return render(
                request, self.template_name, {"form": form, "message": self.message}
            )
        else:
            # no template > logout
            logout(request)
            return redirect("login")

    def post(self, request) -> HttpResponse:
        form = self.form_class(request.POST)
        if form.is_valid():
            # signinForm
            if self.form_class == forms.LoginForm:
                user = authenticate(
                    username=form.cleaned_data["username"],
                    password=form.cleaned_data["password"],
                )
                if user is not None:
                    login(request, user)
                    self.message = f"Welcome {user.username} ! You are connected."
                    return redirect(settings.LOGIN_REDIRECT_URL)
                else:
                    self.message = "Wrong credentials."

            # signupForm
            elif self.form_class == forms.SignupForm:
                user = form.save()
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)

        return render(
            request, self.template_name, {"form": form, "message": self.message}
        )
