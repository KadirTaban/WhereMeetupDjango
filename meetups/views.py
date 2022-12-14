from django.shortcuts import render, redirect

from .forms import RegistrationForm
from meetups.models import Meetup
# Create your views here.

def index(request):
    meetups = Meetup.objects.all()
    
    return render(request,'meetups/index.html',{
        'meetups': meetups
         })

def meetup_details(request, meetup_slug):
    try:
        print("test1")
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            print("test2")
            registration_form = RegistrationForm()
        else:
            print("test3")

            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant = registration_form.save()
                selected_meetup.participants.add(participant)
                return render(request, "meetups/registration-success.html")
                
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found':True,
            'meetup': selected_meetup, 
            'form':registration_form
            })
    except Exception as exc:
        print(exc)
        return render(request,'meetups/meetup-details.html',{
            'meetup_found':False,
        })


def confirm_registration(request):
    return render(request, "meetups/registration-success.html")