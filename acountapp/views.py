from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from acountapp.models import BonBon


def hello_world(request):
    if request.method=='POST':

           temp = request.POST.get('hello_world_input')

           new_bonbon = BonBon()
           new_bonbon.text = temp
           new_bonbon.save()

           return HttpResponseRedirect(reverse('acountapp:hello world'))
    else:
           hello_world_list = BonBon.objects.all()
           return render(request,'accountapp/hello_world.html',
                         context={'hello_world_list':hello_world_list})
