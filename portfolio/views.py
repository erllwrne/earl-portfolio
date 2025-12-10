from django.shortcuts import render
from .models import Profile

def home(request):
    # Get first profile (assuming you have only one profile)
    profile = Profile.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'portfolio/home.html', context)

