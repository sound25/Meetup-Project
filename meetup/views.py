from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import Meetup, Participant
from .forms import RegistrationForm
# Create your views here.
def index(request):
    meetups=Meetup.objects.all()
    return render(request,'meetup/index.html',{'meetups':meetups})

def meetup_detail(request,slug):
    try:
        selected_meetup=Meetup.objects.get(slug=slug)
        if request.method=='GET':
            
            registration_form=RegistrationForm()
            
        else:
            registration_form=RegistrationForm(request.POST)
            if registration_form.is_valid():
                '''
                particiapnt=registration_form.save()
                selected_meetup.participants.add(particiapnt)
                return redirect('confirm_registration')
                '''
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm_registration', slug=slug)

        return render(request,'meetup/meetup_details.html',{
                'meetup':selected_meetup,
                'meetup_found':True,
                'form':registration_form
            })
    except Exception as exc:
        return render(request,'meetup/meetup_details.html',{
            'meetup_found':False
        })

def confirm_registration(request,slug):

    #return render(request,'meetup/registration-success.html')
    meetup = Meetup.objects.get(slug=slug)

    return render(request, 'meetup/registration-success.html', {
        'organizer_email': meetup.organizer_email
    })

    #https://github.com/academind/django-practical-guide-course-code/blob/summary-14-finished/meetups/static/meetups/styles/registration-confirmation.css