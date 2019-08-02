from django.conf.urls import url

from group.views import Grouplist, Vpnsession, Groupconfig

urlpatterns = [
    url('^grouplist$', Grouplist),
    url('^vpnsession$', Vpnsession),
    url('^groupconfig$', Groupconfig),
]
