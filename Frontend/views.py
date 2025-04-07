from django.shortcuts import render,redirect
from BVapp.models import courseDB
from Frontend.models import admissionDb,contactDb
from django.contrib import messages
# Create your views here.
def homepage (req):
    data=courseDB.objects.all()
    return render(req,"homepage.html",{'data':data})

def coursepage(req,Cid):
    data = courseDB.objects.all()
    cata = courseDB.objects.get(id=Cid)
    return render(req, "coursedetails.html", {'data': data, 'cata': cata})
def admissionpage(req):
    return render(req,"addmission.html")

def saveadmission(req):
    if req.method == "POST":
        a = req.POST.get('name')
        b = req.POST.get('course')
        c = req.POST.get('number')
        d = req.POST.get('email')
        e = req.POST.get('message')
        obj=admissionDb(name=a,course=b,number=c,email=d,message=e)
        obj.save()
        messages.success(req, "Admission Conformed")
        return redirect(homepage)

def savecontact(req):
    if req.method == "POST":
        a = req.POST.get('Cname')

        b = req.POST.get('Cnumber')
        c = req.POST.get('Cemail')
        d = req.POST.get('Cmessage')
        obj = contactDb(Cname=a, Cnumber=b, Cemail=c, Cmessage=d)
        obj.save()
        messages.success(req, "Thanks for Contacting Us")
        return redirect(homepage)
