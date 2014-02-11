from django.contrib import admin
from core import models

admin.site.register(models.Morsel)
admin.site.register(models.MorselEventType)
admin.site.register(models.MorselEvent)
admin.site.register(models.ReminderSchedule)
admin.site.register(models.ReminderTask)

