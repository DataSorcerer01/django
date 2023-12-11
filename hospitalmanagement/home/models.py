from django.db import models

# Create your models here.

class Doctor(models.Model):
    name=models.CharField(max_length=20)
    speciality=models.CharField(max_length=10)
    address=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    reports=models.FileField()

    def __str__(self):
        return self.name
    
class Consultation(models.Model):
    patient_name=models.CharField(max_length=100)
    doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appointment_date=models.DateTimeField()

    def __str__(self):
        return f"{self.patient_name}-{self.doctor_id}"

