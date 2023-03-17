from django.contrib import admin
from django.urls import path,include
from resume import views

urlpatterns = [
    path('', views.home, name='home'),
    path('templateview/<int:myid>',views.templateview,name='templateview'),
    path('checkout/<int:myid>',views.checkout,name='checkout'),
    path('check/<int:myid>',views.check,name='check'),
    path('login/',views.handlelogin,name="login"),
    path('signup/',views.handlesignup,name="signup"),
    path('logout/',views.handlelogout,name="logout"),
    path('myorders/',views.bookings,name="booking"),
    path('profile/',views.profile,name="profile"),

    

]
