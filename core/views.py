import markdown
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from core.models import Morsel

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
    fields = ['title', 'content']

    def form_valid(self, form):
        title = form.cleaned_data['title']
        content = markdown.markdown(
                form.cleaned_data['content'],
                safe_mode='escape',
                extensions=['nl2br']
        )
        user = self.request.user
        self.model.objects.create(
                title=title, content=content, user=self.request.user)
        return HttpResponseRedirect(self.get_success_url())
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
