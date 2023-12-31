"""
URL configuration for fotoblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from authentication.views import AuthView
from blog.views import BlogView
from authentication import forms as authForms
from blog import forms as blogForms
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', LoginView.as_view( template_name='auth/login.html', redirect_authenticated_user=True ), name='login'),
    # path('logout/', authentication.views.logout_page, name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path(
        "",
        AuthView.as_view(
            form_class=authForms.LoginForm, template_name="auth/login.html"
        ),
        name="login",
    ),
    path("logout/", AuthView.as_view(), name="logout"),
    path(
        "signup/",
        AuthView.as_view(
            form_class=authForms.SignupForm, template_name="auth/signup.html"
        ),
        name="signup",
    ),
    path(
        "profile/<int:id>/",
        login_required(
            BlogView.as_view(
                form_class=blogForms.ProfileForm, template_name="blog/profile.html"
            )
        ),
        name="profile"
    ),
    path(
        "home/",
        login_required(
            BlogView.as_view(
                form_class=blogForms.BaseForm, template_name="blog/home.html"
            )
        ),
        name="home",
    ),
    path(
        "photos/add/",
        login_required(
            BlogView.as_view(
                form_class=blogForms.PhotoForm, template_name="blog/photo_upload.html"
            )
        ),
        name="photo-upload",
    ),
    path(
        "photos/<int:id>/delete/",
        login_required(BlogView.as_view()),
        name="photo-delete",
    ),
    # Admin interface
    path("admin/", admin.site.urls),
    # Django debug toolbar
    path("__debug__/", include("debug_toolbar.urls"))
]

# DEV MODE only: files at settings.MEDIA_ROOT are served at settings.MEDIA_URL ('media/')
# same for STATIC_ROOT files with settings.STATIC_URL ('static/')
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
