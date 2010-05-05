from django.http import HttpResponse
from letters.models import Letter, Organization
from django.shortcuts import render_to_response, get_object_or_404
from letters.social_media import get_mentions

def home(request):
    list = Letter.objects.all()
    return render_to_response("list.html", locals())


def org_page(request, org):
    organization = get_object_or_404(Organization, name=org)
    mentions = get_mentions(org)
    return render_to_response("org.html", locals())