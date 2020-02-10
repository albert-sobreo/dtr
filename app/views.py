from django.shortcuts import render, HttpResponse, render_to_response, redirect
from app.models import DTR
from datetime import datetime
from django.db.models import Sum

# Create your views here.
def dtr(request):
    hours = {
        "time": DTR.objects.all(),
        "total": DTR.objects.all().aggregate(Sum("diff"))
    }
    return render(request, "index.html", hours)

def addTime(request):
    if request.method == "POST":
        dtr = DTR()

        dtr.date = datetime.strptime(request.POST['date'], '%Y-%m-%d')

        dtr.time_in = datetime.strptime(request.POST['time-in'], '%H:%M')
        dtr.time_out = datetime.strptime(request.POST['time-out'], '%H:%M')

        dtr.diff = dtr.time_out - dtr.time_in

        dtr.save()
        
        return redirect('/')


    else:
        return HttpResponse('invalid')