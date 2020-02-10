from django.shortcuts import render, HttpResponse, render_to_response, redirect, HttpResponseRedirect
from app.models import DTR, Account
from datetime import datetime
from django.db.models import Sum
from django.contrib.auth import logout

# Create your views here.
def dtr(request):
    if request.session.is_empty():
        return redirect('/login/')
    hours = {
        "time": Account.objects.get(username=request.session.get('username')),
        "total": Account.objects.get(username=request.session.get('username')).dtr.aggregate(Sum("diff"))
    }
    return render(request, "index.html", hours)

def addTime(request):
    username = request.session.get('username')
    account = Account.objects.get(username=username)
    if request.method == "POST":
        dtr = DTR()

        dtr.date = datetime.strptime(request.POST['date'], '%Y-%m-%d')

        dtr.time_in = datetime.strptime(request.POST['time-in'], '%H:%M')
        dtr.time_out = datetime.strptime(request.POST['time-out'], '%H:%M')

        dtr.diff = dtr.time_out - dtr.time_in

        dtr.save()

        account.dtr.add(dtr)
        
        return redirect('/')


    else:
        return HttpResponse('invalid')

def loginpage(request):
    if not request.session.is_empty():
        return redirect('/')
    else:
        return render(request, "login.html", )

def registerpage(request):
    if not request.session.is_empty():
        return redirect('/')
    else:
        return render(request, "register.html", )

def registerproc(request):
    if request.method == "POST":
        username = request.POST['username']

        account = Account()

        account.username = username
        account.save()

    return redirect('/login/')

def loginproc(request):
    if request.method == "POST":
        username = request.POST['username']

        request.session['username'] = username
        request.session.save()

        return redirect('/')

def logoutview(request):
    logout(request)
    return HttpResponseRedirect('/login/')