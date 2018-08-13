from django.apps import AppConfig
import os
import signal
import subprocess
from django_proto import settings


class BokehServerConfig(AppConfig):
    """
    this class controls the server
    superclass AppConfig .ready() method starts the server at run time
    """
    name = 'bokeh_server'
    bokeh_bin = settings.BOKEH_BIN
    base_cmd = f"{bokeh_bin} serve"
    plot_dir = settings.MEDIA_ROOT
    process = None

    @staticmethod
    def _start():
        """
        start the bokeh server according to parameters in Django root settings
        grab latest plots from bokeh_plot models
        these plots are loaded as Bokeh apps
        """
        from bokeh_plots import models  # required import statement
        cmd = BokehServerConfig.base_cmd
        # get server url components
        ip = settings.DJANGO_SERVER_IP
        port = settings.DJANGO_SERVER_PORT
        # get all currently available plots from bokeh_plot models
        bokeh_plots = models.Bokeh.objects.all()
        for plot in bokeh_plots:
            cmd += f" {plot.script.file}"  # activate each plot as app
        cmd += f" --allow-websocket-origin={ip}:{port}"  # allow Django access
        print(cmd)
        # The os.setsid() is passed in the argument preexec_fn so
        # it's run after the fork() and before  exec() to run the shell.
        BokehServerConfig.process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                                 shell=True, preexec_fn=os.setsid)
        print("started Bokeh server")

    @staticmethod
    def _kill():
        os.killpg(os.getpgid(BokehServerConfig.process.pid), signal.SIGTERM)
        print("killed the bokeh server")

    @staticmethod
    def restart():
        BokehServerConfig._kill()
        BokehServerConfig._start()

    def ready(self):
        BokehServerConfig._start()
