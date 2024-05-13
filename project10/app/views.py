from django.shortcuts import render
from django.http import HttpResponse
from app.forms import*
# Create your views here.

def register(request):
    EUFO = UserForm()
    EPFO = Profileform()
    d ={'EUFO':EUFO,'EPFO':EPFO}
    if request.method == "POST"  and request.FILES:
        UFDO = UserForm(request.POST)
        PFDO = Profileform(request.POST,request.FILES)
        if UFDO.is_valid():
            MUFDO = MUFDO.save(commit=False)
            pw = UFDO.cleaned_data.get('password')
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO = PFDO.save(commit=False)
            MPFDO.username = MUFDO
            MPFDO.save()
            return HttpResponse("Regisration Complete")
        return HttpResponse("Invalid Data")
    return render(request ,'register.html',d)
