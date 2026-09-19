from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse("Hello Django!")

# def hello(request):
#     return HttpResponse("<h1>Hello</h1><a href ='about/'>visit link</a>")
    
    
# def about(request):
#     return HttpResponse("<h2>it is my about section</h2> <a href ='/'><button>go to home page</button></a>")
    
# def contact(request):
#     return HttpResponse("<h1>This is my contact number.<br> +911452425</h1>")

# def service(request):
#     return HttpResponse("<h1> our services</h1>")

# def post(request):
#     return HttpResponse("<h1>no post here!</h1>")  



def login(request):
    return render(request,"login.html")

def home(request):
      return render(request,"home.html")

def product1(request):
      return render(request,"product1.html")

def product2(request):
      return render(request,"product2.html")

def product3(request):
      return render(request,"product3.html")




def remove(request):
      data = request.GET.get('text',"")
      remove = request.GET.get('remove',"")
      uppercase = request.GET.get('uppercase',"")
      lowercase = request.GET.get('lowercase',"")
      removeline = request.GET.get('removeline',"")
      analyzed=""
      if remove == "on":
            punc = '''!()[]{}:;'"\/|,><.?@#$%^&*_-~'''
            for char in data:
                  if char not in punc:
                        analyzed = analyzed + char

                        print(analyzed)
      if uppercase == "on":
            data = data.upper() 
            analyzed = analyzed + data
       
      if lowercase == "on":
                  data = data.lower() 
                  analyzed = analyzed + data

      if removeline == "on":
           for char in data:
                 if char != "/n":
                       analyzed = analyzed+char

      return render(request,'remove.html',{'changetext':analyzed,'Text':data,})     
      