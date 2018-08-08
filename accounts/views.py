from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html')
