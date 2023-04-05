from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def inset_topic(request):
    tn=input('enter topic name: ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('topic_name is inserted')

def inset_webpage(request):
    tn=input('enter topic name: ')
    wn=input('enter player name: ')
    wu=input('enter player url : ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    wo=Webpage.objects.get_or_create(topic_name=to,name=wn,url=wu)[0]
    to.save()
    wo.save()
    return HttpResponse('topic_name is inserted')


def inset_Accessrecord(request):
    tn=input('enter topic name: ')
    wn=input('enter player name: ')
    wu=input('enter player url : ')
    au=input('enter author name :')
    date=input('enter date :')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    wo=Webpage.objects.get_or_create(topic_name=to,name=wn,url=wu)[0]
    ao=Accessrecord.objects.get_or_create(name=wo,author=au,date=date)[0]
    to.save()
    wo.save()
    ao.save()
    return HttpResponse('topic_name is inserted')