from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from acountapp.models import BonBon


def hello_world(request):
    if request.method=='POST':

           temp = request.POST.get('hello_world_input')

           new_bonbon = BonBon()
           new_bonbon.text = temp
           new_bonbon.save()

           return render(request, 'accountapp/hello_world.html',
                         context={'hello_world_output':new_bonbon})
    else:
           return render(request,'accountapp/hello_world.html',
                         context={'text':' POST METHOD!'})
