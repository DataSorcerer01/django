from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('doctor/',views.doctor,name="doctor"),
    path('book_consultation/',views.book_consultation,name="book_consultation"),
     path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    
]