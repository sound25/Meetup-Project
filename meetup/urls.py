from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='all-meetups'),
    path('<slug:slug>/success', views.confirm_registration,name='confirm_registration'),
    path('<slug:slug>',views.meetup_detail,name='meetup_detail'),
    
]