from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        to=Topic.objects.get_or_create(topic_name=tn)[0]
        to.save()
        return HttpResponse("data inserted into topic successfully.....")
    return render(request,'insert_topic.html')
def insert_webpage(request):
    TOL=Topic.objects.all()
    d={'topic':TOL}
    if request.method=='POST':
        
        tn=request.POST['tn']
        n=request.POST['n']
        ul=request.POST['ul']
        to=Topic.objects.get(topic_name=tn)
        wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=ul)[0]
        wo.save()
        return HttpResponse("data inserted into webpage!!!!!!!!!!!!")
    return render(request,'insert_webpage.html',d)
def insert_access(request):
    AOL=Webpage.objects.all()
    d1={'webpage':AOL}
    if request.method=='POST':
        na=request.POST['na']
        a=request.POST['a']
        d=request.POST['d']
        wo=Webpage.objects.get(name=na)
        ao=AccessRecord.objects.get_or_create(name=wo,author=a,date=d)[0]
        ao.save()
        return HttpResponse("data inserted into accessrecords ...........")
    return render(request,'insert_access.html',d1)