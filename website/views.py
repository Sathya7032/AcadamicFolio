from django.shortcuts import render,redirect
from django.conf import settings
from .models import Contact, Post, Category
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def index(request):
    if request.method=="POST":
        username = request.POST["username"]
        email = request.POST["email"]
        service = request.POST["subject"]
        message1 = request.POST["message1"]
        query = Contact(username=username, email=email, service = service, message1= message1)
        query.save()

        subject = 'welcome to AcadamicFolio'
        message = f'Hi {username}, thank you for showing your intrest in AcadamicFolio. '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )

        
        subject = 'YOU GOT A NEW ORDER'
        message = f'Hi k satyanarayana chary,  Your new customer details are:- \n username - {username},\n service - {service},\n  email - {email},\n message - {message1} \n'
        email_from = settings.EMAIL_HOST_USER
        recipient_list1 = ['charysatheesh4@gmail.com', ]
        send_mail( subject, message, email_from, recipient_list1 )
        messages.success(request,"Thanks for contacting me ,I will get back to you soon....")
        return redirect("/#contact")
        
     
    return render(request,"index.html")

def blog(request):
    posts = Post.objects.all()[:11]

    cats = Category.objects.all()
    data={
        'posts':posts,
        'cats' : cats
    }
    return render(request,"home.html",data)

def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    print(post)
    return render(request,'posts.html',{'post':post, 'cats': cats})


def category(request, url):
    cate = Category.objects.get(url=url)
    posts = Post.objects.filter(cate=cate)
    return render(request, "category.html", {'cate': cate, 'posts': posts})
