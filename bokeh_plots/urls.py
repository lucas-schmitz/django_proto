from django.conf.urls import url
from bokeh_plots import views

app_name = "bokeh_plots"

urlpatterns = [
    url(r"^bokeh_plots$", views.home, name="bokeh_plots_home"),
    url(r"^bokeh_plots/model_form_upload$", views.model_form_upload, name="model_form_upload"),
    # url(r'^bokeh_plots/bokeh_plot/(?P<name>\w+)/$', views.bokeh_plot, name="bokeh_plot")
    url(r"^bokeh_plots/(?P<id>[0-9]+)$", views.bokeh_plot, name="bokeh_plot")
]