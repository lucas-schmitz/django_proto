from django.shortcuts import render, redirect
from bokeh_plots import models
from django.core.files.storage import FileSystemStorage
from bokeh_plots import forms
from bokeh_server.apps import BokehServerConfig
from bokeh.embed import server_session, server_document
from bokeh.util import session_id

# Create your views here.
def home(request):
    bokeh_plots = models.Bokeh.objects.all()
    return render(request, "bokeh_plots/home.html", {"bokeh_plots": bokeh_plots})


def model_form_upload(request):
    if request.method == 'POST':
        form = forms.DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # restart the Bokeh server
            BokehServerConfig.restart()
            return redirect('/bokeh_plots')
    else:
        form = forms.DocumentForm()
    return render(request, 'bokeh_plots/model_form_upload.html', {
        'form': form
    })


def bokeh_plot(request, id):
    bokeh_plot_model = models.Bokeh.objects.get(id=id)
    bokeh_server_url = bokeh_plot_model.get_url()
    server_script = server_document(bokeh_server_url)
    context = {
        "name": bokeh_plot_model.name,
        "server_script": server_script
    }
    return render(request, 'bokeh_plots/bokeh_plot.html', context)
