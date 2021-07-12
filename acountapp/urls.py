from django.urls import path

from acountapp.views import hello_world, AccountCreateView

app_name = 'acountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello world'),

    path('create/', AccountCreateView.as_view(), name='create')
]

