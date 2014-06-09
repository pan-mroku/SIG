# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def zaloguj(request):
    if not request.user.is_authenticated():
        return render(request, 'zaloguj.html')
    else:
        informacja = u"You are already logged in!"
        return render(request, 'index.html', {'info':informacja})
    
def logowanie(request):
    if not request.user.is_authenticated():
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                informacja = u"Hello. You have just logged in."
                return render(request, 'index.html', {'info':informacja})
            else:
                info = 'Account inactive.'
                return render(request, 'zaloguj.html', {'info':info})
        else:
            info2 = u"Wrong login or password!"
            return render(request, 'zaloguj.html', {'info':info2})
    else:
        informacja = u"You are already logged in!"
        return render(request, 'zaloguj.html', {'info':informacja})
        
def zarejestruj(request):
    if not request.user.is_authenticated():
        return render(request, 'zarejestruj.html')
    else:
        informacja = u'You are already registered!'
        return render(request, 'index.html', {'info':informacja})


def rejestracja(request):
    if not request.user.is_authenticated():
        nazwa = request.POST['user_name']
        haslo = request.POST['user_password']
        haslo1 = request.POST['user_password1']
        if (haslo == haslo1):
            if (nazwa != "") and (haslo != ""):
                try:
                    uzytkownik = User.objects.create_user(nazwa, '',haslo)
                    uzytkownik.save()
                    informacja = u"You have succesfully registered!"
                    return render(request, 'index.html', {'info':informacja})
                except:
                    informacja = u"This login is already taken!"
                    return render(request, 'zarejestruj.html', {'info':informacja})
            else:
                informacja = u"You didn't specify login or password."
                return render(request, 'zarejestruj.html', {'info':informacja})
        else:
            informacja = u"Passwords don't match!"
            return render(request, 'zarejestruj.html', {'info':informacja})
    else:
        informacja = u"You are already registered!"
        return render(request, 'index.html', {'info':informacja})
     
def wyloguj(request):
    if request.user.is_authenticated():
        logout(request)
        # Redirect to a success page.
        informacja = u"Logged out!"
        return render(request, 'index.html', {'info':informacja})
    else:
        info = u"You are not logged in!"
        return render(request, 'index.html', {'info':info})
