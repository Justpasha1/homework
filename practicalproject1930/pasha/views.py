from django.shortcuts import render
from practicalapp.models import ProgrammingLanguage
# Create your views here.
def Show_Pashok(request):
    variable = ProgrammingLanguage.objects.all()
    return render(request, 'pasha.html', context={'language':variable})