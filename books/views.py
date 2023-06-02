from django.shortcuts import render

# Create your views here.
def mainPage(request):
    return HttpResponse("main Page")

def mainPageTemplate(request):
    return render(request,"main.html")
def recipeLogin(request):
    return render(request,"main/recipe_detail.html")
def recipeLoginProcess(request):
    username=request.POST.get("username")
    password=request.POST.get("password")

    user=authenticate(request=request,username=username,password=password)
    if user is not None:
        login(request=request,user=user)
        return HttpResponseRedirect(reverse("main_home"))
    else:
        messages.error(request,"Error in Login! Invalid Login Details!")
        return HttpResponseRedirect(reverse("main_login"))
