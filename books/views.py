from django.shortcuts import render

# Create your views here.
def demoPage(request):
    return HttpResponse("main Page")

def demoPageTemplate(request):
    return render(request,"main.html")
def adminLogin(request):
    return render(request,"admin_templates/signin.html")
def adminLoginProcess(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
