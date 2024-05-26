from django import forms
from django.forms import ModelForm,Select
from .models import Studentdetails





class studentform(ModelForm):
    class Meta:
        model =Studentdetails


        fields =("FirstName","LastName","Age","DOB","Email","PhoneNumber","Course","ParentName","Address","image")


        labels={
            "FirstName":"First Name",
            "LastName":"Last Name",
            "Age":"Age",
            "DOB":"Date of Birth",
            "Email":"Email",
            "PhoneNumber":"Phone Number",
            "Course":"Course Name",
            "ParentName":"Parent Name",
            "Address":"Address",
            "image":"Profile Picture",
        }

        
        widgets ={
            #we use form-controls is for bootstrap class
            'FirstName':forms.TextInput(attrs={'class':'form-control','placeholder':'Insert First Name Here'}),
            'LastName':forms.TextInput(attrs={'class':'form-control','placeholder':'Insert Last Name Here'}),
            'Age':forms.TextInput(attrs={'class':'form-control','placeholder':'Insert Age  Here'}),
            'DOB':forms.TextInput(attrs={'class':'form-control','placeholder':'Insert Date of Birth Here'}),
            'Email':forms.TextInput(attrs={'class':'form-control','placeholder':'Insert Email Here'}),
            'PhoneNumber':forms.TextInput(attrs={'class':'form-control','placeholder':'Insert Phone Number Here'}),
            'Course':Select(attrs={'class':'form-control','placeholder':'Insert Course Name Here'}),
            
            'ParentName':forms.TextInput(attrs={'class':'form-control','placeholder':'add email_ad'}),
            'Address':forms.TextInput(attrs={'class':'form-control','placeholder':'add email_address'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'add email_address'}),
       
        }


        
    def __init__(self, *args, **kwargs):
        super(studentform, self).__init__(*args, **kwargs)
        self.fields['Course'].empty_label = "Select an option below"



