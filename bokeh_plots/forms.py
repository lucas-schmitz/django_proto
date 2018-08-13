from django import forms

from bokeh_plots import models
import os


class DocumentForm(forms.ModelForm):
    class Meta:
        model = models.Bokeh
        fields = ('name', 'script',)

