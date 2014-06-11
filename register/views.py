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
    if not request.user.is_authenticated():
        return render(request, 'login-form.html')
    else:
        information = u"You are logged already!"
        return render(request, 'index.html', {'info':information})
    
def loginprocess(request):
    if not request.user.is_authenticated():
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                information = u"Logged in."
                return render(request, 'index.html', {'info':information})
            else:
                info = 'Account is not active'
                return render(request, 'login-form.html', {'info':info})
        else:
            info2 = u"Wrong login or passowrd!"
            return render(request, 'login-form.html', {'info':info2})
    else:
        information = u"You are logged already!"
        return render(request, 'login-form.html', {'info':information})
        
def registerform(request):
    if not request.user.is_authenticated():
        return render(request, 'register.html')
    else:
        information = u'You are logged alredy! Please logout.'
        return render(request, 'index.html', {'info':information})


def registerprocess(request):
    if not request.user.is_authenticated():
        nazwa = request.POST['user_name']
        haslo = request.POST['user_password']
        haslo1 = request.POST['user_password1']
        if (haslo == haslo1):
            if (nazwa != "") and (haslo != ""):
                try:
                    uzytkownik = User.objects.create_user(nazwa, '',haslo)
                    uzytkownik.save()
                    usertype = UserType.objects.create(name=nazwa)
                    usertype.save()
                    information = u"Register done!"
                    return render(request, 'index.html', {'info':information})
                except Exception as e:
                    information = u"Username already exists!"
                    return render(request, 'register.html', {'info':e})
            else:
                information = u"Check your login or password."
                return render(request, 'register.html', {'info':information})
        else:
            information = u"Password didn`t match!"
            return render(request, 'register.html', {'info':information})
    else:
        information = u"You already registered!"
        return render(request, 'index.html', {'info':information})
     
def logoutprocess(request):
    if request.user.is_authenticated():
        logout(request)
        # Redirect to a success page.
        information = u"Logout finished."
        return render(request, 'index.html', {'info':information})
    else:
        information = u"You are not logged in!"
        return render(request, 'index.html', {'info':information})
