from django.conf.urls import url

from users.views import Login, get_img_code, generate_token

urlpatterns = [
    url('^login$', Login),
    url('^get_img_code$', get_img_code),
    url('^generate_token$', generate_token),
]
