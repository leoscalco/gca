from __future__ import unicode_literals

from django.db import models

# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name