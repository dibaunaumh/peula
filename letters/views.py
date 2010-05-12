from django.http import HttpResponse
from letters.models import Letter, Organization
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from letters.social_media import get_mentions
from django.core import serializers
from letters.forms import LetterForm

def home(request):
    list = Letter.objects.all()
    return render_to_response("list.html", locals())


def org_page(request, org):
    organization = get_object_or_404(Organization, name=org)
    mentions = get_mentions(org)
    return render_to_response("org.html", locals())



def search_similar_letters(request, prefix):
    letters = Letter.objects.filter(subject__contains=prefix)
    json = serializers.serialize("json", letters)
    return HttpResponse(json)


def add_letter(request):
    if request.POST:
        form = LetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = LetterForm()
    return render_to_response("edit_letter.html", locals())