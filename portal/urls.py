from django.conf.urls import url
from . import views

app_name = 'portal'

urlpatterns = [
    # /portal/
    url(r'^$', views.index, name='index'),
]