from django.shortcuts import render
from datetime import datetime
from .models import Product

# Create your views here.


def product(request):
    product = Product.objects.all()
    return render(request,'blog/blog.html',{'product':product})

# def blog(request):
#     return render(request,"blog/blog.html")

# class User:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# def home(request):
    context ={
        "name" :"Neha",
         "age" : 21,
         "skills":["python","django","React"],
         "user" :User("aman",2),
         "blog":{
             "author":{
                 "name":"mohit kumar",
             },
             "content":"this is bold",
             "created_at": datetime(2025,8,18,10,30)
         },
         "empty_value":None,


    }

    return render(request,"blog/blog.html",context)