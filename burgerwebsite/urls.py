from . import views
from django.urls import path, re_path, include
app_name= 'burgerwebsite'
urlpatterns = [
    path('', views.index, name='home'),
    #re_path(r'^home/$', views.index, name='home'),
    path('products/', views.products, name='products'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('shop/', views.shop, name='shop'),
    path('signup/', views.signup, name='signup'),
    path("login", views.login_request, name="login"),
    path('contactus/', views.contactus, name='contactus'),
   # path("", views.homepage, name="homepage"),

]

