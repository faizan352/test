from django.shortcuts import render, redirect, render_to_response
# Create your views here.
from django.http import HttpResponse
from .models import *
import csv

def home(request):
    return HttpResponse("RUNNING YOUR PROJECT")


def home1(request):
    return render(request, 'test.html')


def test(request):
    if request.method == "POST":
        obj1 = Class(name=request.POST['class'])
        obj1.save()
        obj = students(request.POST['address'])
        obj.save()
        return HttpResponse("your database has been insert")


def home5(request):
    return render(request, 'user.html')


def user(request):
    if request.method == "POST":
        name = request.POST['name']
        a = Users(name=name, )
        a.save()

        return HttpResponse("data saved")


def home2(request):
    return render(request, 'tsk.html')


def tsk(request):
    if request.method == "POST":
        User = Users.objects.get(id=2)
        name = request.POST['name']
        typ = request.POST['typ']
        due_date = request.POST['due_date']
        description = request.POST['description']
        status = request.POST['status']
        priority = request.POST['priority']
        assign_to = request.POST['assign_to']
        created_by = request.POST['created_by']
        f = TaskDetails(Users=User, name=name, typ=typ, due_date=due_date, description=description, status=status,
                        priority=priority, assign_to=assign_to, created_by=created_by)
        f.save()
        return HttpResponse("Your data has been save successfully")




def user_get(request):
    obj = TaskDetails.objects.get(id=6)
    context = {
        "object": obj
    }
    return render(request, "user_get.html", context)






def home3(request):
    return render(request, 'tsk_view.html')


def tsk_view(request):
    test1 = TaskDetails.objects.get(id=5)
    test1.name = "Akhter"
    test1.save()
    return HttpResponse(test1.created_by)


def home4(request):
    return render(request, 'tsk_cmnt.html')


def tsk_cmnt(request):
    z1 = CommentTask.objects.get(id=2)
    z1.comment = "what a task"
    z1.save()
    return HttpResponse(z1.comment)




# def create(request):
#     if request.method == 'POST':
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/success/url/')