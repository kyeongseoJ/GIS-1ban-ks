from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import BonBon


def hello_world(request):
    if request.method=='POST':

           temp = request.POST.get('hello_world_input')

           new_bonbon = BonBon()
           new_bonbon.text = temp
           new_bonbon.save()

           return HttpResponseRedirect(reverse('accountapp:hello world'))
    else:
           hello_world_list = BonBon.objects.all()
           return render(request,'accountapp/hello_world.html',
                         context={'hello_world_list':hello_world_list})



class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'



class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url =reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
           return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

    def post(self, request, *args, **kwargs):
         if request.user.is_authenticated:
             return super().post(request, *args, **kwargs)
         else:
             return HttpResponseRedirect(reverse('accountapp:login'))


class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url =reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
           return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))
