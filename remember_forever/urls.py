from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^morsel/create/$', 'core.views.create_morsel', name='morsel_create'),
    url(r'^morsel/(?P<pk>\d+)/$', 'core.views.morsel_detail', name='morsel_detail'),
    url(r'^morsel/(?P<pk>\d+)/delete/$', 'core.views.morsel_delete', name='morsel_delete'),
    url(r'^accounts/login/', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),
    url(r'^accounts/', include('registration.backends.default.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
