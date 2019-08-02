from django.conf.urls import url

from server.views import Info, Status, Setpwd, Ssl, Cipher, Hub, Tcp

urlpatterns = [
    url('^info$', Info),
    url('^status$', Status),
    url('^setpwd$', Setpwd),
    url('^ssl$', Ssl),
    url('^cipher$', Cipher),
    url('^hub$', Hub),
    url('^tcp$', Tcp),
]
