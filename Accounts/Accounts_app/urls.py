from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.register,name="register"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('add_products/',views.add_products,name="add_products"),
    path('product_list/',views.product_list,name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    
    
]


