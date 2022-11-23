from django.shortcuts import render
from Game_Distribution.models import UserModel
from django.contrib import messages
from Game_Distribution.forms import Userforms 
from django.db import connection

def homepage(request):
    return render(request, 'homepage.html')

def showuser(request):
    showall  = UserModel.objects.all()
    return render(request,'Index.html',{"data":showall})

def Insertuser(request):
    if request.method=="POST":
        if request.POST.get('User_ID') and request.POST.get('name') and request.POST.get('Age') and request.POST.get('Email') and request.POST.get('PhoneNumber'):
            saverecord=UserModel()
            saverecord.User_ID=request.POST.get('User_ID')
            saverecord.Name=request.POST.get('name')
            saverecord.Age=request.POST.get('Age')
            saverecord.Email=request.POST.get('Email')
            saverecord.PhoneNumber=request.POST.get('PhoneNumber')
            saverecord.save()
            messages.success(request,'User with id: '+saverecord.User_ID+ ' registered Successfully..!')
            return render(request,'Insert.html')
    else:
            return render(request,'Insert.html')

def EditUser(request,id):
    editUserobj=UserModel.objects.get(User_ID=id)
    return render(request,'Edit.html',{"UserModel":editUserobj})

def UpdateUser(request,id):
    UpdateUser=UserModel.objects.get(User_ID=id)
    form=Userforms(request.POST,instance=UpdateUser)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Updated Successfully..!')
        return render(request,'Edit.html',{"UserModel":UpdateUser})

def DelUser(request,id):
    delUser=UserModel.objects.get(User_ID=id)
    delUser.delete()
    showdata=UserModel.objects.all()
    return render(request,"index.html",{"data":showdata})

def runQuery(request):
    raw_query = "select * from dvgd_3_12.user where name like 'J%';"
    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()
    return render(request,'runQuery.html',{'data':alldata})

def sortuser(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=UserModel.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request,'sortuser.html',context)
    else:
        return render(request,'sortuser.html')