from django.shortcuts import render
from practicalapp.models import ProgrammingLanguage
# Create your views here.
def DimaView(request):
    list_lan = ProgrammingLanguage.objects.all()
    return render(request,"dimaapp/dima.html",context={"list_lan":list_lan})