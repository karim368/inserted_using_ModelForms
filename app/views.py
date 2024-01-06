from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
from app.forms import *

def insert_topic(request):
    ETOB = TopicForm()
    d = {'ETOB':ETOB}
    if request.method == 'POST':
        TO = TopicForm(request.POST)
        if TO.is_valid():
            TO.save()
            return HttpResponse('Data inserted successfully')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWOB = WebpageForm()
    d = {'EWOB':EWOB}
    if request.method == 'POST':
        WO = WebpageForm(request.POST)
        if WO.is_valid():
            WO.save()
            return HttpResponse('Data inserted successfully')
    return render(request,'insert_webpage.html',d)

def insert_records(request):
    EROB = AccessRecordsForm()
    d = {'EROB':EROB}
    if request.method == 'POST':
        RO = AccessRecordsForm(request.POST)
        if RO.is_valid():
            RO.save()
            return HttpResponse('Data inserted successfully')
    return render(request,'insert_records.html',d)