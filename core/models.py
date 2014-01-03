from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)


class Morsel(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey('auth.user')

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('morsel_detail', kwargs={'pk': self.id})

    def __unicode__(self):
        return "%s-%s" % (self.user, self.title)


class ReminderDelay(models.Model):
    days = models.IntegerField()
    recurring = models.BooleanField(default=False)

    class Meta:
        ordering = ['days']

    def __unicode__(self):
        return "%s%d days" % ('every ' if self.recurring else '', self.days)


class Reminder(BaseModel):
    morsel = models.ForeignKey(Morsel)
    delay = models.ForeignKey(ReminderDelay)

    def __unicode__(self):
        return "%s after %d days" % (self.morsel, self.delay.days)
