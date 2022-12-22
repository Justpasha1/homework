from django.shortcuts import render
from practicalapp.models import*

# Create your views here.
def show_prohor(request):
    return render(request, "prohor.html", context={"list":list})

