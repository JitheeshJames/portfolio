from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Achievements, Catagories, User_Comments, Project


# Create your views here.

def index(requests):
    projects = Project.objects.all()
    c_lists = Achievements.objects.all()
    cat_lists = Catagories.objects.all()
    return render(requests,'index.html',{'c_lists':c_lists,'cat_lists':cat_lists,'projects':projects})

def user_feedback(requests, msg=None):
    if requests.method == "POST":
        name = requests.POST['name']
        email = requests.POST['email']
        subject = requests.POST['subject']
        message = requests.POST['message']

        feedback= User_Comments.objects.create(name=name,email=email,subject=subject,message=message)
        feedback.save()
        msg = "Thanks for the feedback, will get back to you soon ! "
        return HttpResponseRedirect('/')

    return render(requests,'index.html',{'msg':msg})

def proj_display(requests,id):
    #id = Project.object.get(id=id)
    p_page = Project.objects.get(id=id);
    print(p_page)

    return render(requests,'projectdetails.html',{'id':id,'project':p_page})