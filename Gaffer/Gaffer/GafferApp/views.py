from django.shortcuts import render
from django.http import HttpResponse
from GafferApp.models import Coach,Drill,CoachProfile,CoachingPlan,Player,Lineup

def index(request):
    my_dict = {'insert_me':"Hello this is from view.py!"}
    return render(request,'GafferApp/homePage.html',context = my_dict)
# Create your views here.
def help(request):
    my_help = {'insert_help': "This is going to be your help page"}
    return render(request,'GafferApp/help.html',context = my_help)
