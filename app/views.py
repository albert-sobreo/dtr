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

        dtr.desc = request.POST['desc']

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

def edit(request, dtr_id):
    dtr = DTR.objects.get(id=dtr_id)
    myshit = {
        "id": dtr.id,
        "date": dtr.date,
        "time_in": dtr.time_in,
        "time_out": dtr.time_out,
        "desc": dtr.desc,
    }
    return render(request, "edit.html", myshit)

def editproc(request, dtr_id):
    dtr = DTR.objects.get(id=dtr_id)
    if request.method == "POST":
        date = request.POST['date']
        time_in = request.POST['time_in']
        time_out = request.POST['time_out']
        desc = request.POST['desc']

        dtr.date = datetime.strptime(date, '%Y-%m-%d')
        dtr.time_in = datetime.strptime(time_in, '%H:%M')
        dtr.time_out = datetime.strptime(time_out, '%H:%M')
        dtr.desc = desc
        dtr.diff = dtr.time_out - dtr.time_in

        dtr.save()

    return redirect('/')

def deleteproc(request, dtr_id):
    dtr = DTR.objects.get(id=dtr_id).delete()
    return redirect('/')