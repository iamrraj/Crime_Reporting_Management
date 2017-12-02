from django.conf.urls import url, include
from django.views.generic import TemplateView
from .views import login_view, dashboard
urlpatterns = [

    url(r'^$', login_view , name='login'),

    url(r'^dashboard/$', dashboard , name='dashboard'),

]

