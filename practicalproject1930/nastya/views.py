from django.shortcuts import render
from practicalapp.models import ProgrammingLanguage

def show_nastya(request):
    listlanguage = ProgrammingLanguage.objects.all()
    return render(request, 'nastya.html',context={'listlanguages':listlanguage})
