# Create your views here.
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from register.models import UserType

def loginform(request):
    isWorker=False
    if not request.user.is_authenticated():
        return render(request, 'login-form.html')
    else:
        information = u"You are logged already!"
        usertype = UserType.objects.get(name=request.user.username)
        isWorker = usertype.isWorker
        return render(request, 'index.html', {'info':information, 'isWorker':isWorker})
    
def loginprocess(request):
    isWorker=False
    if not request.user.is_authenticated():
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                information = u"Logged in."
                usertype = UserType.objects.get(name=request.user.username)
                isWorker = usertype.isWorker
                return render(request, 'index.html', {'info':information, 'isWorker':isWorker})
            else:
                info = 'Account is not active'
                return render(request, 'login-form.html', {'info':info, 'isWorker':isWorker})
        else:
            info2 = u"Wrong login or passowrd!"
            return render(request, 'login-form.html', {'info':info2, 'isWorker':isWorker})
    else:
        information = u"You are logged already!"
        return render(request, 'login-form.html', {'info':information, 'isWorker':isWorker})
        
def registerform(request):
    isWorker=False
    if not request.user.is_authenticated():
        return render(request, 'register.html')
    else:
        information = u'You are logged alredy! Please logout.'
        return render(request, 'index.html', {'info':information, 'isWorker':isWorker})


def registerprocess(request):
    worker=False
    if not request.user.is_authenticated():
        nazwa = request.POST['user_name']
        haslo = request.POST['user_password']
        haslo1 = request.POST['user_password1']
        if (haslo == haslo1):
            if (nazwa != "") and (haslo != ""):
                try:
                    uzytkownik = User.objects.create_user(nazwa, '',haslo)
                    uzytkownik.save()
                    if nazwa == 'worker':
                      worker=True

                    usertype = UserType.objects.create(name=nazwa, isWorker=worker)					
                    usertype.save()
                    information = u"Register done!"
                    return render(request, 'index.html', {'info':information, 'isWorker':worker})
                except Exception as e:
                    information = u"Username already exists!"
                    return render(request, 'register.html', {'info':e, 'isWorker':worker})
            else:
                information = u"Check your login or password."
                return render(request, 'register.html', {'info':information, 'isWorker':worker})
        else:
            information = u"Password didn`t match!"
            return render(request, 'register.html', {'info':information, 'isWorker':worker})
    else:
        information = u"You already registered!"
        return render(request, 'index.html', {'info':information, 'isWorker':worker})
     
def logoutprocess(request):
    isWorker=False
    if request.user.is_authenticated():
        logout(request)
        # Redirect to a success page.
        information = u"Logout finished."
        return render(request, 'index.html', {'info':information, 'isWorker':isWorker})
    else:
        information = u"You are not logged in!"
        return render(request, 'index.html', {'info':information, 'isWorker':isWorker})
