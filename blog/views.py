from multiprocessing.managers import BaseManager
import string
from django.forms import Form
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import resolve
from django.views.generic import View
from . import forms, models


class BlogView(View):
    form_class: Form = forms.BaseForm
    template_name: string = ''
    message = ''
    id = 0

    def get(self, request, **kwargs) -> HttpResponse:
        form = self.form_class()
        viewName = self.getViewName(request)
        photos: BaseManager[models.Photo] = []
        if 'home' in request.path:
            photos = models.Photo.objects.all()
        context = {'form': form, 'photos': photos, "viewName": viewName}
        return render(request, self.template_name, context=context)

    def post(self, request, **kwargs) -> HttpResponse:
        form = self.form_class(request.POST, request.FILES)
        viewName = self.getViewName(request)
        context = {'form': form, "viewName": viewName}
        # Bill + photo upload
        if 'blog/create' in self.template_name:
            blog_form = forms.AddBillForm(request.POST)
            photo_form = forms.PhotoForm(request.POST, request.FILES)
            if all([blog_form.is_valid, photo_form.is_valid]):
                photo = photo_form.save(commit=False)
                photo.uploader = request.user
                photo.save()
                blog = blog_form.save(commit=False)
                blog.author = request.user
                # link photo to blog
                blog.photo = photo
                blog.save()
                context = {
                    'blog_form': blog_form,
                    'photo_form': photo_form,
                    'viewName': viewName
                }
        # Photo upload
        elif 'photo_upload' in self.template_name:
            photo = form.save(commit=False)
            #  add uploader ID before save()
            photo.uploader = request.user
            photo.save()
            form.save()
            return redirect('home')

        return render(request, self.template_name, context=context)

    def delete(self, request, id: int) -> HttpResponse:
        if 'photo' in request.path:
            elt = models.Photo.objects.get(id=id)
            elt.delete()
            return JsonResponse({'message': 'Photo deleted successfully', 'code': 200})

    def getViewName(self, request) -> str:
        l_path = request.path
        l_view = resolve(l_path)
        return l_view.view_name
