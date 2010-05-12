from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.sites.models import Site

class Organization(models.Model):
    name = models.CharField(_("name"), max_length=255, unique=True, db_index=True)
    email = models.EmailField(_("email"))
    fax_number = models.CharField(_("fax"), max_length=100, null=True, blank=True)
    url = models.URLField(_("url"), null=True, blank=True, verify_exists=False)

    def get_absolute_url(self):
        domain_name = Site.objects.get(id=settings.SITE_ID)
        return "http://%s/organization/%s/" % (domain_name, self.name)

    class Metaclass:
        verbose_name = _("organization")
        verbose_name_plural = _("organizations")


    def __unicode__(self):
        return self.name
    


class Letter(models.Model):
    author = models.ForeignKey(User, verbose_name=_("author"), db_index=True)
    organization = models.ForeignKey(Organization, verbose_name=_("organization"))
    subject = models.CharField(_("subject"), max_length=255)
    content = models.TextField(_("content"), max_length=4000)

    def get_absolute_url(self):
        domain_name = Site.objects.get(id=settings.SITE_ID)
        return "http://%s/letter/%d/" % (domain_name, self.id)

    def __unicode__(self):
        return "%s: %s" % (self.author.username, self.subject)

    class Metaclass:
        verbose_name = _("letter")
        verbose_name_plural = _("letters")