from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from .models import Profile,Post,Uploadworkoutvideo,Blog,Bodyweight,Recepies
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate,login,logout
from django.utils.deprecation import MiddlewareMixin
import os
from django.shortcuts import get_object_or_404

def index(request):
    post = Post.objects.all().order_by('-id')
    video = Uploadworkoutvideo.objects.all().order_by('-id')
    if request.method == "GET":
        st = request.GET.get('servicename')

        if st != None:
            post = Post.objects.filter(description__icontains=st)
            video = Uploadworkoutvideo.objects.filter(titleofvideo__icontains=st)
    return render(request,'index.html',{'post':post,'video':video})


def services(request):
 services = Post.objects.all()
 if request.method == "GET":
  st = request.GET.get('servicename')
  if st != None:
   services = Post.objects.filter(description__icontains=st)
 return render(request,'services.html',{'services': services})


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        image = request.FILES['image']
        user = User.objects.create_user(username=username, password=password)
        profile = Profile.objects.create(user=user, profile_picture=image)
        if profile:
            messages.success(request, 'Profile Created Please Login')
            return redirect("loggedin")

    return render(request,'signup.html')


def loggedin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")




    return render(request,'loggedin.html')


def Logout(request):
    logout(request)
    return redirect("loggedin")


def uploadpost(request):
    if request.method == 'POST':
        user = request.user
        image = request.FILES['image']
        description = request.POST['description']
        profile = Profile.objects.get(user=user)
        posts = Post.objects.create(user=user, image=image, description=description, profile=profile)
        if posts:
            messages.success(request, 'Post Uploaded')
    return render(request, 'uploadposts.html')


def uploadworkout(request):
    if request.method == 'POST':
        user = request.user
        profile = Profile.objects.get(user=user)
        video = request.FILES['video']
        titleofvideo = request.POST['titleofvideo']
        dietdescription = request.POST['dietdescription']
        country = request.POST['country']
        day = request.POST['day']
        muscle = request.POST['muscle']
        uploadworkout = Uploadworkoutvideo(user=user, video=video, titleofvideo=titleofvideo,
                                           dietdescription=dietdescription
                                           , country=country, day=day, muscle=muscle, profile=profile)
        uploadworkout.save()

    return render(request,'uploadworkout.html')


def viewvideo(request,id):
    video = Uploadworkoutvideo.objects.filter(id=id)[0]
    vidview = video.viewss + 1
    video_up = Uploadworkoutvideo.objects.filter(id=id).update(viewss=vidview)
    return render(request,'viewvideo.html',{'video':video})

def like(request,id):
    video = Uploadworkoutvideo.objects.get(id=id)

    if request.user in video.ping.all():
        video.ping.remove(request.user)

    else:
        video.ping.add(request.user)

    return render(request,'viewvideo.html',{'video':video})


def workouts(request):
    video = Uploadworkoutvideo.objects.all()
    if request.method == "GET":
        st = request.GET.get('servicenamee')
        if st != None:
            video = Uploadworkoutvideo.objects.filter(titleofvideo__icontains=st)
    return render(request,'workouts.html',{'video':video})


def workoutsmonday(request):
    video = Uploadworkoutvideo.objects.filter(day='Monday')
    if request.method == "GET":
        st = request.GET.get('servicenamee')
        if st != None:
            video = Uploadworkoutvideo.objects.filter(titleofvideo__icontains=st).filter(day='Monday')
    return render(request,'app/monday.html',{'video':video})

def workoutstuesday(request):
    video = Uploadworkoutvideo.objects.filter(day='Tuesday')
    if request.method == "GET":
        st = request.GET.get('servicenamee')
        if st != None:
            video = Uploadworkoutvideo.objects.filter(titleofvideo__icontains=st).filter(day='Tuesday')
    return render(request,'app/tuesday.html',{'video':video})

def workoutswednesday(request):
    video = Uploadworkoutvideo.objects.filter(day='Wednesday')
    if request.method == "GET":
        st = request.GET.get('servicenamee')
        if st != None:
            video = Uploadworkoutvideo.objects.filter(titleofvideo__icontains=st).filter(day='Wednesday')
    return render(request,'app/wednesday.html',{'video':video})


def workoutsthursday(request):
    video = Uploadworkoutvideo.objects.filter(day='Thursday')
    if request.method == "GET":
        st = request.GET.get('servicenamee')
        if st != None:
            video = Uploadworkoutvideo.objects.filter(titleofvideo__icontains=st).filter(day='Thursday')
    return render(request,'app/thursday.html',{'video':video})

def workoutsfriday(request):
    video = Uploadworkoutvideo.objects.filter(day='Friday')
    if request.method == "GET":
        st = request.GET.get('servicenamee')
        if st != None:
            video = Uploadworkoutvideo.objects.filter(titleofvideo__icontains=st).filter(day='Friday')
    return render(request,'app/friday.html',{'video':video})


def workoutssaturday(request):
    video = Uploadworkoutvideo.objects.filter(day='Saturday')
    if request.method == "GET":
        st = request.GET.get('servicenamee')
        if st != None:
            video = Uploadworkoutvideo.objects.filter(titleofvideo__icontains=st).filter(day='Saturday')
    return render(request,'app/saturday.html',{'video':video})

def workoutssunday(request):
    video = Uploadworkoutvideo.objects.filter(day='Sunday')
    if request.method == "GET":
        st = request.GET.get('servicenamee')
        if st != None:
            video = Uploadworkoutvideo.objects.filter(titleofvideo__icontains=st).filter(day='Sunday')
    return render(request,'app/sunday.html',{'video':video})

def arms(request):
    video = Uploadworkoutvideo.objects.filter(muscle='Arms')
    if request.method == "GET":
        st = request.GET.get('servicenamee')
        if st != None:
            video = Uploadworkoutvideo.objects.filter(titleofvideo__icontains=st).filter(muscle='Arms')
    return render(request,'muscle/arms.html',{'video':video})

def abscore(request):
    video = Uploadworkoutvideo.objects.filter(muscle='Abs')
    if request.method == "GET":
        st = request.GET.get('servicenamee')
        if st != None:
            video = Uploadworkoutvideo.objects.filter(titleofvideo__icontains=st).filter(muscle='Abs')
    return render(request,'muscle/abs.html',{'video':video})


def back(request):
    video = Uploadworkoutvideo.objects.filter(muscle='Back')
    if request.method == "GET":
        st = request.GET.get('servicenamee')
        if st != None:
            video = Uploadworkoutvideo.objects.filter(titleofvideo__icontains=st).filter(muscle='Back')
    return render(request,'muscle/back.html',{'video':video})

def biceps(request):
    video = Uploadworkoutvideo.objects.filter(muscle='Biceps')
    if request.method == "GET":
        st = request.GET.get('servicenamee')
        if st != None:
            video = Uploadworkoutvideo.objects.filter(titleofvideo__icontains=st).filter(muscle='Biceps')
    return render(request,'muscle/biceps.html',{'video':video})


def chest(request):
    video = Uploadworkoutvideo.objects.filter(muscle='Chest')
    if request.method == "GET":
        st = request.GET.get('servicenamee')
        if st != None:
            video = Uploadworkoutvideo.objects.filter(titleofvideo__icontains=st).filter(muscle='Chest')
    return render(request,'muscle/chest.html',{'video':video})

def triceps(request):
    video = Uploadworkoutvideo.objects.filter(muscle='Triceps')
    if request.method == "GET":
        st = request.GET.get('servicenamee')
        if st != None:
            video = Uploadworkoutvideo.objects.filter(titleofvideo__icontains=st).filter(muscle='Triceps')
    return render(request,'muscle/triceps.html',{'video':video})


def legs(request):
    video = Uploadworkoutvideo.objects.filter(muscle='Legs')
    if request.method == "GET":
        st = request.GET.get('servicenamee')
        if st != None:
            video = Uploadworkoutvideo.objects.filter(titleofvideo__icontains=st).filter(muscle='Legs')
    return render(request,'muscle/legs.html',{'video':video})


def shoulders(request):
    video = Uploadworkoutvideo.objects.filter(muscle='Shoulders')
    if request.method == "GET":
        st = request.GET.get('servicenamee')
        if st != None:
            video = Uploadworkoutvideo.objects.filter(titleofvideo__icontains=st).filter(muscle='Shoulders')
    return render(request,'muscle/shoulders.html',{'video':video})


def bodyweight(request):
    if request.method == 'POST':
        user = request.user
        bodyvideo = request.FILES['bodyvideo']
        title = request.POST['title']
        profile = Profile.objects.get(user=request.user)

        bodyweightworkout = Bodyweight(user=user,bodyvideo=bodyvideo,title=title,profile=profile)
        bodyweightworkout.save()
    return render(request,'bodyweight.html')


def bodyweightworkout(request):
    video = Bodyweight.objects.all()
    if request.method == "GET":
        st = request.GET.get('servicenamee')
        if st != None:
            video = Bodyweight.objects.filter(title__icontains=st)
    return render(request,'bodyweightworkout.html',{'video':video})



def uploadrecepies(request):
    if request.method == 'POST':
        user = request.user
        recepievideo = request.FILES['recepievideo']
        recepietitle = request.POST['recepietitle']
        instructions = request.POST['instructions']
        preptime = request.POST['preptime']
        cooktime = request.POST['cooktime']
        ingredients = request.POST['ingredients']
        tools = request.POST['tools']
        profile = Profile.objects.get(user=request.user)

        recepies = Recepies(user=user,recepievideo=recepievideo,recepietitle=recepietitle,instructions=instructions,
                            preptime=preptime,cooktime=cooktime,ingredients=ingredients,tools=tools,profile=profile)
        recepies.save()
    return render(request,'uploadrecepies.html')


def viewvideobodyweight(request,id):
    video = Bodyweight.objects.filter(id=id)[0]
    vidview = video.viewss + 1
    video_up = Bodyweight.objects.filter(id=id).update(viewss=vidview)
    return render(request,'viewvideobodyweight.html',{'video':video})









def recepies(request):
    recepies = Recepies.objects.all().order_by('-id')
    if request.method == "GET":
        st = request.GET.get('servicenamee')
        if st != None:
            recepies = Recepies.objects.filter(recepietitle__icontains=st)
    return render(request,'recepies.html',{'recepies':recepies})




def singlerecepies(request,id):
    recepie = Recepies.objects.filter(id=id)[0]
    vidview = recepie.viewss + 1
    video_up = Recepies.objects.filter(id=id).update(viewss=vidview)
    return render(request,'singlerecepies.html',{'recepie':recepie})



def userprofile(request,id):
    profile = Post.objects.get(id=id)
    profuser = Profile.objects.get(user=profile.user)
    posts = Post.objects.filter(user=profile.user)
    video = Uploadworkoutvideo.objects.filter(user=profile.user)
    recepies = Recepies.objects.filter(user=profile.user)
    return render(request,'profile.html',{'posts':posts,'video':video,'profuser':profuser,'recepies':recepies})


def userprofilevid(request,id):
    workvid = Uploadworkoutvideo.objects.get(id=id)
    profuser = Profile.objects.get(user=workvid.user)
    posts = Post.objects.filter(user=workvid.user)
    video = Uploadworkoutvideo.objects.filter(user=workvid.user)
    recepies = Recepies.objects.filter(user=workvid.user)
    return render(request,'profile.html',{'posts':posts,'video':video,'profuser':profuser,'recepies':recepies})



def following(request,id):
    following = Profile.objects.get(id=id)
    profile = Post.objects.get(id=id)
    profuser = Profile.objects.get(user=profile.user)
    posts = Post.objects.filter(user=profile.user)
    video = Uploadworkoutvideo.objects.filter(user=profile.user)
    recepies = Recepies.objects.filter(user=profile.user)

    if request.user in following.followings.all():
        following.followings.remove(request.user)

    else:
        following.followings.add(request.user)

    return render(request,'profile.html',{'following':following,'posts':posts,'video':video,'profuser':profuser,'recepies':recepies})

def listfollowers(request,id):
    profile = Profile.objects.get(id=id)
    followers = profile.followings.all()

    print(followers)
    context = {
        'profile':profile,
        'followers':followers,
    }
    return render(request,'listfollowers.html',{'followers':followers,'profile':profile})


def loginprofile(request):
    profile  = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(user=request.user)
    video = Uploadworkoutvideo.objects.filter(user=request.user)
    recepies = Recepies.objects.filter(user=request.user)
    return render(request,'loginprofile.html',{'profile':profile,'posts':posts,'video':video,'recepies':recepies})


def profileofollowers(request,id):
    profile = Profile.objects.get(id=id)
    #vlog = VlogPost.objects.filter(user=profile.user)
    post = Post.objects.filter(user=profile.user)
    #profile = Post.objects.get(id=id)
    #profuser = Profile.objects.get(user=profile.user)
    #posts = Post.objects.filter(user=profile.user)
    video = Uploadworkoutvideo.objects.filter(user=profile.user)
    recepies = Recepies.objects.filter(user=profile.user)
    return render(request,'profileofollowers.html',{'profile':profile,'post':post,'video':video,'recepies':recepies})
