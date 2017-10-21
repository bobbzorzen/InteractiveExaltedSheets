from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cards/$', views.cards, name='cards'),
    url(r'^$', views.index, name='index')
]