from django.conf.urls import url, include
from locking import views

urlpatterns = [
    # verwijst naar een ajax-view voor het lockingmechanisme
    url(r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/lock/$', views.lock),
    url(r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/unlock/$', views.unlock),
    url(r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/is_locked/$', views.is_locked),
    # url(r'variables\.js$', 'js_variables', {}, views.locking_variables),
]

urlpatterns += [
    url(r'jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': 'locking'}),
]