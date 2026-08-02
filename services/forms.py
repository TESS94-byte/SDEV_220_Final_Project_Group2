from django import forms
from .models import Customer, Appointment


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer

        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
        ]

        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email Address",
            "phone": "Phone Number",
        }



class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = [
            "service",
            "appointment_date",
            "appointment_time",
        ]

        labels = {
            "service": "Cleaning Service",
            "appointment_date": "Preferred Date",
            "appointment_time": "Preferred Time",
        }


        widgets = {

            "appointment_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),


            "appointment_time": forms.TimeInput(
                attrs={
                    "type": "time",
                }
            ),

        }