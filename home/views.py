from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def gallerys(request):
    return render(request,"gallery-single.html")

def gallery(request):
    return render(request,"gallery.html")

def sip(request):
    return render(request,"sample-inner-page.html")

def services(request):
    return render(request,"services.html")