from django.conf.urls import url
from . import views

urlpatterns = [
    url('index', views.home),
    url('^article/(?P<id_article>\d+)/$', views.view_article),

]
