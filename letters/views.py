from django.http import HttpResponse
from letters.models import Letter, Organization
from django.shortcuts import render_to_response, get_object_or_404
from letters.social_media import get_mentions
from django.core import serializers


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
