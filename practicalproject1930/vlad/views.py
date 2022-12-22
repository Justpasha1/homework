from django.shortcuts import render
from practicalapp.models import ProgrammingLanguage


def show_vlad(request): 
    program = ProgrammingLanguage.objects.all()
    return render(request, 'vlad.html', context={"program":program.name})

   
