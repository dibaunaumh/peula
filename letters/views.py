from django.http import HttpResponse
from letters.models import Letter
from django.shortcuts import render_to_response

def home(request):
    list = Letter.objects.all()
    return render_to_response("list.html", locals())