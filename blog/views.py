from multiprocessing.managers import BaseManager
import string
from django.forms import Form
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from . import forms, models

# from django.contrib.auth.decorators import login_required
# @login_required
# def home(request):
#     return render(request, 'blog/home.html')

class BlogView(View):
    form_class: Form = forms.BaseForm
    template_name: string = ''
    message = ''
    photo_id = 0

    def get(self, request) -> HttpResponse:
        form = self.form_class()
        photos: BaseManager[models.Photo] = []
        if 'home' in request.path:
            photos = models.Photo.objects.all()
        return render(request, self.template_name, {'form':form, 'photos':photos})

    def post(self, request, **kwargs) -> HttpResponse:
        form = self.form_class(request.POST, request.FILES)
        #  Delete a photo by id
        if 'delete' in request.path and kwargs['photo_id']:
            return self.delete(request, kwargs['photo_id'])
        if form.is_valid():
            # Photo upload
            if 'photo_upload' in self.template_name:
                photo = form.save(commit=False)
                #  add uploader ID before save()
                photo.uploader = request.user
                photo.save()
                return redirect('home')
        return render(request, self.template_name, {'form':form})

    def delete(self, request, photo_id:int) -> HttpResponse:
        elt = models.Photo.objects.get(id=photo_id)
        elt.delete()
        return redirect('home')