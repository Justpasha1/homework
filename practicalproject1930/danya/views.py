from django.shortcuts import render
from practicalapp.models import ProgrammingLanguage
# Create your views here.
def show_danya(request):
    languages = ProgrammingLanguage.objects.all()
    return render(request, 'danya.html', context={'languages':languages})
    



