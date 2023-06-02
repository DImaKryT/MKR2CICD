from django.shortcuts import render

# Create your views here.
def demoPage(request):
    return HttpResponse("main Page")

def demoPageTemplate(request):
    return render(request,"main.html")
def adminLogin(request):
    return render(request,"main/recipe_detail.html")
def adminLoginProcess(request):
    username=request.POST.get("username")
    password=request.POST.get("password")

    user=authenticate(request=request,username=username,password=password)
    if user is not None:
        login(request=request,user=user)
        return HttpResponseRedirect(reverse("main_home"))
    else:
        messages.error(request,"Error in Login! Invalid Login Details!")
        return HttpResponseRedirect(reverse("main_login"))
