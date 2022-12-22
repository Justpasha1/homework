from django.shortcuts import render

# Create your views here.
def show_artem(request):
    return render(request, 'artem.html')

