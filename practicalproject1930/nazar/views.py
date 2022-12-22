from django.shortcuts import render
from practicalapp.models import *

# Create your views here.

def show_nazar(request):
    program = ProgrammingLanguage.objects.all()
    return render(request, 'nazar.html', context={"program":program})
