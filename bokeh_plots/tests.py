import os
from django.test import TestCase
from .models import Bokeh
from bokeh_server import apps
# Create your tests here.
from django_proto import settings
from django.core.files import File
import mock

class SimpleTest(TestCase):
    def tearDown(self):
        super(TestCase, self).tearDown()
        apps.BokehServerConfig._kill()

    def create_bokeh_model(self):
        # script_path = os.path.join(settings.MEDIA_ROOT, "bokeh_test/load_beam.py")
        # self.assertTrue(os.path.isfile(script_path))
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = "test"
        model = Bokeh.objects.create(name="test", script=file_mock)
        return model

    def test_create_model(self):
        first_model = self.create_bokeh_model()
        print(first_model)

