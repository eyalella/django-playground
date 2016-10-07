from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^post_apt/$', views.post_apt, name='post_apt'),
    url(r'^user/(\w+)/$', views.user, name='user'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media\/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }, name='post_apt')
    ]
