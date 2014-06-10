# Create your views here.
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from register.models import UserType

def zaloguj(request):
    if not request.user.is_authenticated():
        return render(request, 'zaloguj.html')
    else:
        informacja = u"Zalogowales sie juz!"
        return render(request, 'index.html', {'info':informacja})
    
def logowanie(request):
    if not request.user.is_authenticated():
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                informacja = u"Zalogowales sie."
                return render(request, 'index.html', {'info':informacja})
            else:
                info = 'Konto nieaktywne'
                return render(request, 'zaloguj.html', {'info':info})
        else:
            info2 = u"Zly uzytkownik lub haslo!"
            return render(request, 'zaloguj.html', {'info':info2})
    else:
        informacja = u"Jestes juz zalogowany!"
        return render(request, 'zaloguj.html', {'info':informacja})
        
def zarejestruj(request):
    if not request.user.is_authenticated():
        return render(request, 'zarejestruj.html')
    else:
        informacja = u'Juz sie zarejestrowales! <a href="/register/wyloguj/">Wyloguj sie</a>'
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
                    usertype = UserType.objects.create(name=nazwa)
                    usertype.save()
                    informacja = u"Zarejestrowales sie!"
                    return render(request, 'index.html', {'info':informacja})
                except Exception as e:
                    informacja = u"Uzytkownik juz istnieje!"
                    return render(request, 'zarejestruj.html', {'info':e})
            else:
                informacja = u"Nie wpisano loginu lub hasla"
                return render(request, 'zarejestruj.html', {'info':informacja})
        else:
            informacja = u"Hasla nie zgadzaja sie!"
            return render(request, 'zarejestruj.html', {'info':informacja})
    else:
        informacja = u"Juz jestes zarejestrowany!"
        return render(request, 'index.html', {'info':informacja})
     
def wyloguj(request):
    if request.user.is_authenticated():
        logout(request)
        # Redirect to a success page.
        informacja = u"Wylogowales sie!"
        return render(request, 'index.html', {'info':informacja})
    else:
        info = u"Nie jestes zalogowany!"
        return render(request, 'index.html', {'info':info})
