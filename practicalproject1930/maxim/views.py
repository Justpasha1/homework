from django.shortcuts import render
from practicalapp.models import ProgrammingLanguage

def show_max(request):
    languages = ProgrammingLanguage.objects.all()
    return render(request, 'maxim2/max.html', context={'languages':languages})

# Create your views here.
