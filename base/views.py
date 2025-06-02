from django.shortcuts import render
from django.conf import settings

# Create your views here.

def index(request):
    context = {
        'WEB3FORMS_ACCESS_KEY': settings.WEB3FORMS_ACCESS_KEY
    }
    return render(request, 'index.html', context)