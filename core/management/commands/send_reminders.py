''' Finds all morsels due for a reminder and sends them. '''
from django.core.management.base import NoArgsCommand, CommandError
from django.core.mail import send_mail
from django.conf import settings
from core import models
from datetime import datetime


class Command(NoArgsCommand):
    help = 'Finds all morsels due for a reminder and sends them.'

    def handle_noargs(self, **options):
        schedule = models.ReminderDelay.objects.values_list('days', flat=True)
        now = datetime.now()
        for morsel in models.Morsel.objects.all():
            days = (now - morsel.created.replace(tzinfo=None)).days
            if days in schedule and not models.Reminder.objects.filter(
                morsel=morsel, delay__days=days
            ).exists():
                send_mail(
                    morsel.title, morsel.content, settings.DEFAULT_FROM_EMAIL,
                    [morsel.user.email], fail_silently=False
                )
                models.Reminder.objects.create(
                    morsel=morsel,
                    delay=models.ReminderDelay.objects.filter(days=days)
                )
            

