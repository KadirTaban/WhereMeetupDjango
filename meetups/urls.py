from django.urls import path
from . import views

urlpatterns = [

    path('meetups/', views.index, name='all-meetups'),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-details'),
    path('meetups/<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),

] 