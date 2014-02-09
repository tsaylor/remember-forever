from datetime import datetime
import pytz
import markdown
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Morsel(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey('auth.user')

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('morsel_detail', kwargs={'pk': self.id})

    @property
    def html_content(self):
        return markdown.markdown(
            self.content,
            safe_mode='escape',
            extensions=['nl2br']
        )

    @property
    def reminded_today(self):
        return self.morselevent_set.filter(
            event_type__code=MorselEventType.REMINDER_SENT,
            event_datetime__gte=datetime.utcnow().replace(tzinfo=pytz.utc)
        ).exists()

    def __unicode__(self):
        return "%s-%s" % (self.user, self.title)


class ReminderSchedule(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)

    DECAYING = 'decaying'

    def __unicode__(self):
        return self.name


class ReminderTask(models.Model):
    delay = models.IntegerField(help_text='delay (in days)')
    repeating = models.BooleanField(default=False)
    schedule = models.ForeignKey(ReminderSchedule)

    def __unicode__(self):
        return "{} day reminder".format(self.delay)

    class Meta:
        ordering = ['delay']


class MorselEventType(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)

    CREATED = 'created'
    SCHEDULE_RESET = 'schedule_reset'
    REMINDER_SENT = 'reminder_sent'

    def __unicode__(self):
        return self.name


class MorselEvent(models.Model):
    morsel = models.ForeignKey('Morsel')
    event_type = models.ForeignKey('MorselEventType')
    event_datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{} on {} at {}'.format(
            self.event_type.name, self.morsel.name, self.event_datetime
        )
