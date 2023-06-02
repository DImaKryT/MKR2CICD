from django.shortcuts import render

# Create your views here.
def demoPage(request):
    return HttpResponse("main Page")

def demoPageTemplate(request):
    return render(request,"main.html")
