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


class MorselForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(), widget=forms.HiddenInput
    )

    class Meta:
        model = Morsel
