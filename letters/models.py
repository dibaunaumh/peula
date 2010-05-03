from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField()
    fax_number = models.CharField(max_length=100, null=True, blank=True)


    def __unicode__(self):
        return self.name
    


class Letter(models.Model):
    author = models.ForeignKey(User, db_index=True)
    organization = models.ForeignKey(Organization)
    subject = models.CharField(max_length=255)
    content = models.TextField(max_length=4000)

    
    def __unicode__(self):
        return "Letter from %s: %s" % (self.author.username, self.subject)
