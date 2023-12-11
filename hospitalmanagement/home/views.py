from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_date
from django.db import IntegrityError
from .models import Doctor, Consultation

# Create your views here.
def home(request):
    return render(request,"home.html")

def doctor(request):
    doctor_list=Doctor.objects.all()
    return render(request,"doctor.html",{'doctor':doctor_list}) 

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')    


def book_consultation(request):
    if request.method == "GET":
        patient_name = request.POST.get('patient_name')
        appointment_date = request.POST.get('appointment_date')
        doctor_id = request.POST.get('doctor_id')

        # Check if patient_name is provided
        if not patient_name:
            message = "Please provide the patient name."
            return render(request, 'book_consultation.html', {'message': message})

        # Check if the doctor is already booked
        if Consultation.objects.filter(doctor_id=doctor_id, appointment_date=appointment_date).exists():
            message = "This doctor is already booked for a consultation on the selected date."
            return render(request, 'book_consultation.html', {'message': message})

        # If the doctor is not booked, proceed with the booking logic
        consultation = Consultation(patient_name=patient_name, doctor_id=doctor_id, appointment_date=appointment_date)
        consultation.save()

        # Redirect to the list of doctors after booking consultation
        doctor_list=Doctor.objects.all() 
        return render(request, 'doctor.html', {'doctor': doctor_list, 'message': 'Consultation booked successfully!'})

    # If the request method is not POST, render the book_consultation.html template
    doctor_list=Doctor.objects.all()  # Query the list of doctors
    return render(request, 'book_consultation.html', {'doctor': doctor_list})