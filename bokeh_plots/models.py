import os
import re
from django_proto import settings
from django.db import models
from django_proto.validators import is_python


# Create your models here.
class Bokeh(models.Model):
    name = models.CharField(max_length=30, unique=True)
    script = models.FileField(upload_to="bokeh_test/", validators=[is_python])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def delete(self, using=None, keep_parents=False):
        if os.path.isfile(self.script.path):
            os.remove(self.script.path)
        super(Bokeh, self).delete()

    def get_url(self):
        """
        return the URL of this model running on Bokeh server
        url syntax: <http(s)>://<bokeh server ip>:<port #>/<bokeh app name>
        :return: url as string
        """
        protocol = settings.BOKEH_SERVER_PROTOCOL
        ip = settings.BOKEH_SERVER_IP
        port = settings.BOKEH_SERVER_PORT
        address = f"{protocol}://{ip}:{port}/{self.bokeh_app_name}"
        return address

    @property
    def bokeh_app_name(self):
        """
        returns the basename of the script
        called by get_url() to construct url address for HTML plot embed
        :return:
        """
        head, tail = os.path.split(self.script.file.__str__())
        app_name = tail[:-3]
        return app_name