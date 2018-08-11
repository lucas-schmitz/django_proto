from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accounts/profile', views.profile),
    url(r'^accounts/bokeh_test', views.bokeh_test)
]
