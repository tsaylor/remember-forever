''' Finds all morsels due for a reminder and sends them. '''
import pytz
from django.core.management.base import NoArgsCommand, CommandError
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from core import models
from datetime import datetime


class Command(NoArgsCommand):
    help = 'Finds all morsels due for a reminder and sends them.'

    def handle_noargs(self, **options):
        schedule = models.ReminderSchedule.objects.get(
            code=models.ReminderSchedule.DECAYING
        )
        tasks = list(schedule.remindertask_set.all())
        now = datetime.utcnow().replace(tzinfo=pytz.utc)
        for morsel in models.Morsel.objects.all():
            days = (now - morsel.created).days
            print 'checking {}-"{}" ({} days)... '.format(
                morsel.user, morsel.title, days),
            for task in tasks:
                if (
                    (task.delay == days or
                        (task.repeating and days % task.delay == 0 and days > 0)
                    ) and
                    not morsel.reminded_today
                ):
                    msg = EmailMultiAlternatives(
                        morsel.title, morsel.content,
                        settings.DEFAULT_FROM_EMAIL, [morsel.user.email],
                    )
                    msg.attach_alternative(morsel.html_content, "text/html")
                    msg.send()

                    models.MorselEvent.objects.create(
                        morsel=morsel,
                        event_type=models.MorselEventType.objects.get(
                            code=models.MorselEventType.REMINDER_SENT
                        )
                    )
                    print "sending {} day reminder".format(task.delay),
            print 

