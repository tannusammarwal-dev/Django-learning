"""
URL configuration for djangolearning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('remove/',views.remove),
    # path("",include("demo.urls")),
    # path("student/",include("demo2.urls")),
    # path('home/' ,views.home, name= 'home'),
    # path('product1/',views.product1,name='product1'),
    # path('product2/',views.product2,name='product2'),
    # path('product3/',views.product3,name='product3')
    
]
