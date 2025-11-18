from django.shortcuts import render,redirect
from . import models
from django.urls import reverse,reverse_lazy
from tweet_app.form import AddTweetForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.

def listtweet(request):
    all_tweets=models.Tweet.objects.all()
    tweet_dict={"tweets":all_tweets}
    return render(request,"tweet_app/listtweet.html",context=tweet_dict)

@login_required(login_url="/login")
def addtweet (request):
    if request.POST:
        message=request.POST["message"]
        models.Tweet.objects.create(username=request.user ,message=message)
        return redirect(reverse('tweetapp:listtweet'))
    else:
        return render(request,"tweet_app/addtweet.html")

def login(request):
     return render(request,'templates/registration/login.html',context={"form":form})

def custom_logout(request):
    logout(request)
    return redirect('/')
def delete(request,id):
    tweet=models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect("tweetapp:listtweet")


class SignUpView(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name="registration/signup.html"
