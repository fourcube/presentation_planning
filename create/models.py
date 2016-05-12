# coding: utf-8
from __future__ import unicode_literals

from django.db import models

from django.conf import settings

# Create your models here.


class Pres(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, default="Neuer Vortrag")
    max_members = models.PositiveSmallIntegerField(default="10")
    room = models.PositiveSmallIntegerField(blank=True)
    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True)

    class Meta:
        verbose_name = "Präsentation"
        verbose_name_plural = 'Präsentationen'

    def __unicode__(self):
        return ("%s - Raum(%s)") % (self.name, self.room)
