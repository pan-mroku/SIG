from django.shortcuts import render,redirect
from models import *
from register.models import UserType
# Create your views here.

def Start(request):
#guest
    e='Done!'
    isWorker=False
    if request.user.is_authenticated():
        usertype = UserType.objects.get(name=request.user.username)
        isWorker = usertype.isWorker
	
    info='Welcome!'
    context={'info':info, 'isWorker':isWorker}
    return render(request, 'index.html', context)
