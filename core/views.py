from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from core.models import Morsel, MorselForm

def home(*args, **kwargs):
    request = args[0]
    if request.user.is_authenticated():
        return user_home(*args, **kwargs)
    else:
        return anon_home(*args, **kwargs)

class AnonHome(TemplateView):
    template_name = 'anon_home.html'

anon_home = AnonHome.as_view()

class UserHome(ListView):
    model = Morsel

    def get_queryset(self):
        return Morsel.objects.filter(user=self.request.user)

user_home = login_required(UserHome.as_view())

class CreateMorsel(CreateView):
    model = Morsel
    form_class = MorselForm

    def get_form_kwargs(self):
        kwargs = super(CreateMorsel, self).get_form_kwargs()
        kwargs.update({'initial':{'user': self.request.user.id}})
        return kwargs

    def get_success_url(self):
        return reverse('home')

create_morsel = login_required(CreateMorsel.as_view())


class MorselDetail(DetailView):
    model = Morsel

morsel_detail = login_required(MorselDetail.as_view())


class MorselDelete(DeleteView):
    model = Morsel
    success_url = reverse_lazy('home')

morsel_delete = login_required(MorselDelete.as_view())
