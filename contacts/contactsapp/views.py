from django.shortcuts import render,redirect
from django.http import HttpResponse
from  .models import Contact



# Create your views here.
def form(request):
    return render(request,"form.html")

def submit(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        msg =request.POST.get('message')

        if name and msg:
            Contact.objects.create(
                name =name,
                email =email,
                message=msg,
            )
            return HttpResponse(f"Thank you {name} for contacting us!")

    return redirect ("form")
                

           

            

        

