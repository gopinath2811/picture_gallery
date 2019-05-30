from django import forms  
from personalApplication.models import Employee  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  


class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Image Name",max_length=50)  
    lastname  = forms.CharField(label="Album Name", max_length = 50)  
    file      = forms.FileField() # for creating file input  