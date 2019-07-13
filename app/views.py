import smtplib
import ssl

from django.shortcuts import render
from .models import *

def RegisterDetails(request):
    name=request.POST.get("name")
    gender=request.POST.get("gender")
    contact=request.POST.get("contact")
    email=request.POST.get("email")
    image=request.FILES["image"]
    username=request.POST.get("username")
    password=request.POST.get("password")
    Registration_Details(name=name,gender=gender,contact=contact,email=email,image=image,username=username,password=password).save()
    return render(request,"Register.html",{"message":name + " Was Successfully Registered"})


def LoginDetails(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    qs=Registration_Details.objects.filter(username=username,password=password)
    if qs:
        id=""
        for x in qs:
            id=x.id
        request.session["status"] = True
        request.session["username"] = username

        return render(request, "UserMainPage.html", {"username":username,"id":id})
    else:
        return render(request, "Login.html", {"messsage": "Username or Password Did not Match"})



def TraineeDetails(request):
    id=request.GET.get("id")
    qs=Add_Trainee_Details.objects.all()
    return render(request,"Trainee.html",{"qs":qs,'id':id})


def gymDetails(request):
    id = request.GET.get('id')
    qs=Add_Gym_Center_Details.objects.all()
    print(id)


    return render(request,"Gym_center.html",{"qs":qs,'id':id})


def Show(request):
    id=request.GET.get("id")
    t=Add_Trainee_Details.objects.filter(id=id)
    if t:
        return render (request,"Show.html",{"qs":t})
    else:
        pass


def Show_Gym(request):
    id=request.GET.get("id")

    qs=Add_Gym_Center_Details.objects.filter(id=id)
    if qs:
        return render(request,"Gym show.html",{"qs":qs})
    else:
        pass


    return None


def UpdateUserProfile(request):
    id=request.GET.get("id")
    qs=Registration_Details.objects.filter(id=id)
    name=""
    gender=""
    contact=""
    email=""
    photo=""
    username=""
    password=""
    for x in qs:
        name=x.name
        gender=x.gender
        contact=x.contact
        email=x.email
        photo=x.image
        username=x.username
        password=x.password
    print(name,gender,contact,email,photo,username,password)

    return render(request,"UserUpdate.html",{"name":name,"gender":gender,"contact":contact,"email":email,"photo":photo,"username":username,"password":password
                                             ,"id":id})


def UserUpdateProfile(request):
    id=request.POST.get("id")
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    contact = request.POST.get("contact")
    email = request.POST.get("email")
    image = request.FILES["image"]
    username = request.POST.get("username")
    password = request.POST.get("password")

    # smtp_server = "smtp.gmail.com"
    # port = 465
    # From_mail = "prasadnaidu766@gmail.com"
    # To_email = email
    # e_password = "ssjjikexxnhftbuk"
    # message = "Hello"+name+","+"Successfully Registred in Gym Management"
    # context = ssl.create_default_context()
    # with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    #     server.login(From_mail, e_password)
    #     server.sendmail(From_mail, To_email, message)

    # email_from="devapatla.sreekanthreddy@gmail.com"
    # email_to=email
    # server=smtplib.SMTP('smtp.gmail.com',587)
    # server.starttls()
    # server.login(email_from,"lynzdcqilyaupzpk")
    # message = "Hello"+name+","+"Successfully Registred in Gym Management"
    # server.sendmail(email_from,email_to,message)
    # server.quit()
    Registration_Details.objects.filter(id=id).update(name=name,gender=gender,contact=contact,email=email,image=image,username=username,password=password)
    return render(request,"UserUpdate.html",{"message":"Successfully Updated"+name+" profile"})


def logout(request):
    del request.session["status"]
    del request.session["username"]
    return render(request,"Index.html")


def Home(request):
    qs=Home_Images.objects.all()

    return render(request,"home.html",{"qs":qs})


def Feed_back(request):
    id= request.GET.get('id')
    return render(request, "Feedback.html",{"id":id})


def FeedbackDetails(request):
    name=request.POST.get("name")
    email=request.POST.get("email")
    message=request.POST.get("message")
    Feedback(name=name,email=email,message=message).save()
    return render(request, "Feedback.html", {"message": "Your feedback Sended Successfully"})


def Contact(request):
    qs=Contact_Us.objects.all()
    return render(request,"ContactUs.html",{"qs":qs})


def ForgetPassword(request):
    type=request.GET.get("type")

    return render(request,"Login.html",{"type":type})


def ForgetDetails(request):
    username=request.POST.get("username")
    print(username)
    qs=Registration_Details.objects.filter(username=username)
    type = "forget_type"
    if qs:
        return render(request,"Login.html",{"type":type})
    else:
        return render(request,"Login.html",{"message":"user name not matched"})


def ResetPassword(request):
    new_password=request.POST.get("password1")
    confirm_password=request.POST.get("password2")
    if new_password==confirm_password:
        Registration_Details.objects.update(password=new_password)
        return render(request,"Login.html",{'message':"Successfully Changed your  Password"})
    else:
        return render(request,"Login.html",{'message':'Your password not matched'})
