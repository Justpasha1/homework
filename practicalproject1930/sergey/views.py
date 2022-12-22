from django.shortcuts import render
from practicalapp.models import ProgrammingLanguage
#Create your views here.

def show_sergey(request):
    list_languages = ProgrammingLanguage.objects.all()
    return render(request,'sergey.html',context={'list_languages':list_languages})

#         .---.
#        |   '.|  __
#        | ___.--'  )
#      _.-'_` _%%%_/
#   .-'%%% a: a %%%
#       %%  L   %%_
#       _%\'-' |  /-.__
#    .-' / )--' #/     '\
#   /'  /  /---'(    :   \
#  /   |  /( /|##|  \     |
# /   ||# | / | /|   \    \
# |   ||##| I \/ |   |   _|
# |   ||: | o  |#|   |  / |
# |   ||  / I  |:/  /   |/
# |   ||  | o   /  /    /
# |   \|  | I  |. /    /
#  \  /|##| o  |.|    /
#   \/ \::|/\_ /  ---'|
#         .---.
#        |   '.|  __
#        | ___.--'  )
#      _.-'_` _%%%_/
#   .-'%%% a: a %%%
#       %%  L   %%_
#       _%\'-' |  /-.__
#    .-' / )--' #/     '\
#   /'  /  /---'(    :   \
#  /   |  /( /|##|  \     |
# /   ||# | / | /|   \    \
# |   ||##| I \/ |   |   _|
# |   ||: | o  |#|   |  / |
# |   ||  / I  |:/  /   |/
# |   ||  | o   /  /    /
# |   \|  | I  |. /    /
#  \  /|##| o  |.|    /
#   \/ \::|/\_ /  ---'|