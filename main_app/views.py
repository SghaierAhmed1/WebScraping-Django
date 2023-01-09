from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Games
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
import django_filters
from django.http import HttpResponse
def blog(request):
    return render(request, "blog.html")
def gamereview(request):
    return render(request, "game-review.html.html")
def index(request):
    l = Games.objects.all()
    return render(request, "index.html", {'Games': l})
def fighter(request):
    l = Games.objects.all()
    return render(request, "fighter.html", {'Games': l})
    return render(request, 'fighter.html')
def sb(request):
    L = Games.objects.filter(price__startswith="30") | Games.objects.filter(price__startswith="31") | Games.objects.filter(price__startswith="32") | Games.objects.filter(price__startswith="33") | Games.objects.filter(price__startswith="34") | Games.objects.filter(price__startswith="35") | Games.objects.filter(price__startswith="36") | Games.objects.filter(price__startswith="37") | Games.objects.filter(price__startswith="38") | Games.objects.filter(price__startswith="39") | Games.objects.filter(price__startswith="£30") | Games.objects.filter(price__startswith="£31") | Games.objects.filter(price__startswith="£32") | Games.objects.filter(price__startswith="£33") | Games.objects.filter(price__startswith="£34") | Games.objects.filter(price__startswith="£35") | Games.objects.filter(price__startswith="£36") | Games.objects.filter(price__startswith="£37") | Games.objects.filter(price__startswith="£38") | Games.objects.filter(price__startswith="£39")
    return render(request, 'single-blog.html',{'Games':L})
def teams(request):
    l = Games.objects.all()
    return render(request, "team.html", {'Games': l})
    return render(request, 'team.html')
def Twenties(request):
    l = Games.objects.filter(price__startswith="20") | Games.objects.filter(price__startswith="21") | Games.objects.filter(price__startswith="22") | Games.objects.filter(price__startswith="23") | Games.objects.filter(price__startswith="24") | Games.objects.filter(price__startswith="25") | Games.objects.filter(price__startswith="26") | Games.objects.filter(price__startswith="27") | Games.objects.filter(price__startswith="28") | Games.objects.filter(price__startswith="29") | Games.objects.filter(price__startswith="£20") | Games.objects.filter(price__startswith="£21") | Games.objects.filter(price__startswith="£22") | Games.objects.filter(price__startswith="£23") | Games.objects.filter(price__startswith="£24") | Games.objects.filter(price__startswith="£25") | Games.objects.filter(price__startswith="£26") | Games.objects.filter(price__startswith="£27") | Games.objects.filter(price__startswith="£28") | Games.objects.filter(price__startswith="£29")
    return render (request,"Twenties.html", {'Games': l})
def Tens(request):
    L = Games.objects.filter(price__startswith="10") | Games.objects.filter(price__startswith="11") | Games.objects.filter(price__startswith="12") | Games.objects.filter(price__startswith="13") | Games.objects.filter(price__startswith="14") | Games.objects.filter(price__startswith="15") | Games.objects.filter(price__startswith="16") | Games.objects.filter(price__startswith="17") | Games.objects.filter(price__startswith="18") | Games.objects.filter(price__startswith="19") | Games.objects.filter(price__startswith="£10") | Games.objects.filter(price__startswith="£11") | Games.objects.filter(price__startswith="£12") | Games.objects.filter(price__startswith="£13") | Games.objects.filter(price__startswith="£14") | Games.objects.filter(price__startswith="£15") | Games.objects.filter(price__startswith="£16") | Games.objects.filter(price__startswith="£17") | Games.objects.filter(price__startswith="£18") | Games.objects.filter(price__startswith="£19")
    return render (request,"Tens.html" , {'Games':L})
def blog (request):
    L = Games.objects.filter(price__startswith="40") | Games.objects.filter(price__startswith="41") | Games.objects.filter(price__startswith="42") | Games.objects.filter(price__startswith="43") | Games.objects.filter(price__startswith="44") | Games.objects.filter(price__startswith="45") | Games.objects.filter(price__startswith="46") | Games.objects.filter(price__startswith="47") | Games.objects.filter(price__startswith="48") | Games.objects.filter(price__startswith="49") | Games.objects.filter(price__startswith="£40") | Games.objects.filter(price__startswith="£41") | Games.objects.filter(price__startswith="£42") | Games.objects.filter(price__startswith="£43") | Games.objects.filter(price__startswith="£44") | Games.objects.filter(price__startswith="£45") | Games.objects.filter(price__startswith="£46") | Games.objects.filter(price__startswith="£47") | Games.objects.filter(price__startswith="£48") | Games.objects.filter(price__startswith="£49")
    return render(request,'blog.html',{'Games': L})
def u10 (request):
    L = Games.objects.filter(price__startswith="1.") | Games.objects.filter(price__startswith="2.") | Games.objects.filter(price__startswith="3.") | Games.objects.filter(price__startswith="4.") | Games.objects.filter(price__startswith="5.") | Games.objects.filter(price__startswith="6.") | Games.objects.filter(price__startswith="7.") | Games.objects.filter(price__startswith="8.") | Games.objects.filter(price__startswith="9.") | Games.objects.filter(price__startswith="£1.") | Games.objects.filter(price__startswith="£2.") | Games.objects.filter(price__startswith="£3.") | Games.objects.filter(price__startswith="£4.") | Games.objects.filter(price__startswith="£5.") | Games.objects.filter(price__startswith="£6.") | Games.objects.filter(price__startswith="£7.") | Games.objects.filter(price__startswith="£8.") | Games.objects.filter(price__startswith="£9.")
    return render (request, 'u10.html', {'Games': L})
def tajrib(request):
    l = Games.objects.all()
    return render(request, "jareb.html", {'Games': l})
    return render(request, 'jareb.html')
def contact (request):
    l = Games.objects.all()
    return render(request, "contact.html", {'Games': l})
    return render(request, 'contact.html')

def logout_view(request):
    logout(request)
    return redirect('index.html')

def search(request):
    q = request.GET.get('q')
    if q:
        products = Games.objects.filter(title__icontains=q)
        if products:
            context = {"Prod": products , "q":q}
            tem = "results.html"
        else:
            tem = "noresult.html"
            context ={"q": q}
    else:
        tem = "nothing.html"
        context ={"q":q}
    return render(request, tem , context,)
def login_view(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():

            u=form.cleaned_data['username']
            p=form.cleaned_data['password']
            user=authenticate(username=u,password=p)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('index.html')

            else:
                return render(request,'login.html',{'form':form})


    else:
        form=LoginForm()
        return render(request,'login.html',{'form':form})
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def GG(request, id):
    # dictionary for initial data with
    # field names as keys
    obj = get_object_or_404(Games, id=id)

    context = {
        "object": obj,

    }
    return render(request, "GG.html", context)

# Create your views here.
