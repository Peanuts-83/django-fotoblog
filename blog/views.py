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
        return render(request, self.template_name, {'form':form, 'photos':photos, "viewName":viewName})

    def post(self, request, **kwargs) -> HttpResponse:
        form = self.form_class(request.POST, request.FILES)
        viewName = self.getViewName(request)
        if form.is_valid():
            # Photo upload
            if 'photo_upload' in self.template_name:
                photo = form.save(commit=False)
                #  add uploader ID before save()
                photo.uploader = request.user
                photo.save()
            form.save()
            return redirect('home')
        return render(request, self.template_name, {'form':form, "viewName":viewName})

    def delete(self, request, id:int) -> HttpResponse:
        if 'photo' in request.path:
            elt = models.Photo.objects.get(id=id)
            elt.delete()
            return JsonResponse({'message':'Photo deleted successfully', 'code':200})

    def getViewName(self, request) -> str:
        l_path = request.path
        l_view = resolve(l_path)
        return l_view.view_name