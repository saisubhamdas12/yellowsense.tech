from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from app2.forms import *
from app2.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def Time_table(request):
    prt=product_from()
    d={'prt':prt}
    if request.method=='POST':
        Tpro=product_from(request.POST)
        if Tpro.is_valid():
            Tpro.save()
        return HttpResponse('data update')
    return render(request,'Time_table.html',d)

def maid(request):
    mdr=product1_from()
    p={'mdr':mdr}
    if request.method=='POST':
        md=product1_from(request.POST)
        if md.is_valid():
            md.save()
        return HttpResponse('data update')
    return render(request,'maid,cook.html',p)



def home(request):
    data1=Time.objects.all()
    data2=Maid_deatails.objects.filter()
    d={'data1':data1,'data2':data2}
    return render(request,'home2.html',d)

def retrieve(request):
    return render(request,'retrivedata.html')

@login_required
def booking(request):
    if request.method=='POST':
        maid=request.POST['maid']
        maidobject=Maid_deatails.objects.get(name=maid)
        date=request.POST['date']
        # dateobj=Maid_deatails.objects.get(Date=date)
        mobile=request.POST['mobile']
        #mobileobject=Maid_deatails.objects.get(phone_number=mobile)
        rating=request.POST['rating']
        #ratingobject=Maid_deatails.objects.get(rating=rating)
        t=request.POST['time']
        Appoint=Booking.objects.get_or_create(time=t,name=maidobject,phone_number=mobile,Date=date,rating=rating)
        
        if Appoint[1]==False:
            return HttpResponse("This is already booked")
        Appoint[0].save()
        return HttpResponse("Booked Successfully")
    return render(request,'nanny.html')
def nanny(request):
    data1=Time.objects.all()
    data2=Maid_deatails.objects.filter()
    d={'data1':data1,'data2':data2}
    return render(request,'nanny.html',d)


def maid2(request):
    data1=Time.objects.all()
    data2=Maid_deatails.objects.filter()
    d={'data1':data1,'data2':data2}
    return render(request,'maid2.html',d)

def cook(request):
    data1=Time.objects.all()
    data2=Maid_deatails.objects.filter()
    d={'data1':data1,'data2':data2}
    return render(request,'cook.html',d)

def About(request):
    return render(request,'About.html')