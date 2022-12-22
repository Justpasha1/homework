from django.shortcuts import render
from practicalapp.models import ProgrammingLanguage
# Create your views here.
def show_roma(request):
    list = ProgrammingLanguage.objects.all()
    return render(request,'roma.html',context={"list":list})
# 