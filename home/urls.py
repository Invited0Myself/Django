
from django.urls import path,include
from .views import index,about,contact,gallerys,gallery,sip,services

urlpatterns = [
    path('',index ,name='index'),
    path('about/',about, name='about' ),
    path('contact/',contact, name='contact' ),
    path('gallerys/',gallerys, name='gellerys' ),
    path('gallery/',gallery, name='gallery' ),
    path('sip/',sip , name='sip'),
    path('services/',services, name='services' ),

]