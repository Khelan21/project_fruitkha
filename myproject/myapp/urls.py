"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cpass/', views.cpass, name='cpass'),
    path('fpass/', views.fpass, name='fpass'),
    path('otp/', views.otp, name='otp'),
    path('newpass/', views.newpass, name='newpass'),
    path('uprofile/', views.uprofile, name='uprofile'),
    path('sindex/', views.sindex, name='sindex'),
    path('sadd/', views.sadd, name='sadd'),
    path('sview/', views.sview, name='sview'),
    path('pdetails/<int:pk>/', views.pdetails, name='pdetails'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('shop/', views.shop, name='shop'),
    path('bppdetails/<int:pk>/', views.bppdetails, name='bppdetails'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('addwish/<int:pk>', views.addwish, name='addwish'),
    path('dwish/<int:pk>', views.dwish, name='dwish'),
    path('cart/', views.cart, name='cart'),
    path('addcart/<int:pk>', views.addcart, name='addcart'),
    path('dcart/<int:pk>', views.dcart, name='dcart'),
    path('changeqty/<int:pk>', views.changeqty, name='changeqty'),
    path('sucess/',views.sucess,name='sucess'),
    path('myorder/',views.myorder,name='myorder'),
    # path('coupon/', views.coupon, name='coupon'),

]


