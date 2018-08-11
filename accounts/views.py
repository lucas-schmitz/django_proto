from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html')


def bokeh_test(request):
    return render(request, 'accounts/bokeh_test.html')
