from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^post_apt/$', views.post_apt, name='post_apt'),
]

if settings.DEBUG:
  urlpatterns += [
    url(r'^media\/(?P<path>.*)$', serve, {
      'document_root': settings.MEDIA_ROOT
    }, name='post_apt')
  ]