from django.shortcuts import render
from practicalapp.models import ProgrammingLanguage
# Create your views here.
def show_german(request):
    programming_language = ProgrammingLanguage.objects.all()
    return render(request, 'german.html', context = {'programming_language':programming_language})
