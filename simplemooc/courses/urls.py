from django.conf.urls import url

from simplemooc.courses.views import index, details

urlpatterns = [
    #url('^$', home, name='home'),
    url('^$', index, name='index'),
    #url('^(?P<pk>\d+)/$', details, name='details'),
    url('^(?P<slug>[\w_-]+)/$', details, name='details'),
]