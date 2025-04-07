from django.shortcuts import render,redirect
from BVapp.models import courseDB
from Frontend.models import admissionDb,contactDb
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def indexpage(req):
    return render(req,"Indexpage.html")
def addcourse(req):
    return render(req,"addcourse.html")

def savecourse(req):
    if req.method == "POST":
        a = req.POST.get('name')
        b = req.POST.get('time')
        c = req.POST.get('description')
        d = req.POST.get('description2')
        e = req.POST.get('price')

        img1 = req.FILES['image']

        obj = courseDB(name=a, time=b, description=c,description2=d, price=e, image=img1, )
        obj.save()
        messages.success(req, "Details Add Successfully")

        return redirect(addcourse)

def displaycourse(req):
    data = courseDB.objects.all()
    return render(req,"displaycourse.html",{'data':data})

def editcourse(req, Cid):
    data = courseDB.objects.get(id=Cid)
    return render(req, "editcourse.html", {'data': data})


def updatecousre(req, Uid):
    if req.method == "POST":
        # Retrieve data from POST request
        a = req.POST.get('name')
        b = req.POST.get('time')
        c = req.POST.get('description')
        d = req.POST.get('description2')
        e = req.POST.get('price')

        # Retrieve the existing details for the given Uid
        try:
            details = courseDB.objects.get(id=Uid)
        except courseDB.DoesNotExist:
            messages.error(req, "Details not found!")
            return redirect(displaycourse)

        # Handle file uploads
        try:
            img1 = req.FILES['image']

            fs = FileSystemStorage()
            file1 = fs.save(img1.name, img1)

        except MultiValueDictKeyError:
            file1 = details.roomimage1


        # Update the database record
        courseDB.objects.filter(id=Uid).update(
            name=a,
            time=b,

            description=c,
            description2=d,
            price=e,
            image=file1,

        )

        messages.success(req, "Details Updated Successfully")
        return redirect(displaycourse)


def deletecourse(req, Delid):
    data = courseDB.objects.filter(id=Delid)
    data.delete()
    messages.warning(req, "Details Deleted Successfully")
    return redirect(displaycourse)



def adminlogin(req):
    return render(req, "adminlogin.html")

def admin(request):
    if request.method == "POST":
        a = request.POST.get('username')
        b = request.POST.get('pass')
        if User.objects.filter(username__contains=a).exists():
            x = authenticate(username=a, password=b)
            if x is not None:
                login(request, x)
                request.session['username'] = a
                request.session['password'] = b
                messages.success(request, "Welcome..")
                return redirect(indexpage)
            else:
                messages.warning(request, "Invaild username or password")
                return redirect(adminlogin)
        else:
            messages.warning(request, "Please check before enter ")
            return redirect(adminlogin)


def adminlogout(req):
    del req.session['username']
    del req.session['password']
    messages.success(req, "Logout Successfully")
    return redirect(adminlogin)


def displayadmission(req):
    data=admissionDb.objects.all()
    return render(req,"displayadmission.html",{'data':data})

def deleteadmission(req, Aid):
    data = admissionDb.objects.filter(id=Aid)
    data.delete()
    messages.warning(req, "Details Deleted Successfully")
    return redirect(displayadmission)


def displaycontact(req):
    cata=contactDb.objects.all()
    return render(req,"displaycontact.html",{'cata':cata})

def deletecontact(req, Cid):
    cata = contactDb.objects.filter(id=Cid)
    cata.delete()
    messages.warning(req, "Details Deleted Successfully")
    return redirect(displaycontact)