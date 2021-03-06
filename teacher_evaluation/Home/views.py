from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Teacher
from django.shortcuts import render

import json


class HomeView(TemplateView):
    template_name = 'Home/home.html'



def get_teachers(request):

    if request.is_ajax():
        q = request.GET.get('term', '')
        teachers = Teacher.objects.filter(name__icontains=q)
        results = [teacher.name for teacher in teachers]
        data = json.dumps(results)
    else:
        data = 'fail'

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def allTeachers(request):
    teachers = Teacher.objects.all()
    return render(request,'home/teachers.html',{'teachers':teachers})