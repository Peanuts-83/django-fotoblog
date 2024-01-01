import string
from django.forms import Form
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import resolve
from authentication import forms

from fotoblog import settings
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View

from authentication.models import User



class AuthView(View):
    form_class: Form = forms.BaseForm
    template_name: string = ""
    message = ""

    def get(self, request, **kwargs) -> HttpResponse:
        form = self.form_class()
        viewName = self.getViewName(request)
        #  GET user profile form
        if 'profile' in request.path:
            form = forms.ProfileForm(instance=request.user)
            return render(request, self.template_name, {"form": form, "message": self.message, "viewName":viewName})
        if len(self.template_name) > 0:
            # user is logged > redirect to home
            if request.user.is_authenticated:
                return redirect('home')
            # else allow signin process
            return render(
                request, self.template_name, {"form": form, "message": self.message, "viewName":viewName}
            )
        else:
            # no template > logout
            logout(request)
            return redirect("login")

    def post(self, request, **kwargs) -> HttpResponse:
        form = self.form_class(request.POST)
        viewName = self.getViewName(request)
        # Update user profile
        if 'profile' in request.path:
            form = self.form_class(request.POST, request.FILES, instance=request.user)
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

            # profile update form
            elif self.form_class == forms.ProfileForm:
                userProfile = get_object_or_404(User, id=kwargs['id'])
                oldPhoto = userProfile.photo_profile
                # delete old photo from disk if changed
                if oldPhoto and 'photo_profile' in form.changed_data:
                    oldPhoto.delete()
                form.save()
                return redirect('home')

        return render(
            request, self.template_name, {"form": form, "message": self.message, "viewName":viewName}
        )

    def getViewName(self, request) -> str:
        l_path = request.path
        l_view = resolve(l_path)
        return l_view.view_name