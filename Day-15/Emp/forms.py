from Emp.models import UsrRg,NewData
from django import forms 



class UsregForm(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields=['username','email','password']
		widgets={"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username","required":True,}),
		"password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password","required":True,}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Email-Id","required":True,}),}

class Userupdate(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields=['username','email','age']
		widgets={"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Update Username","required":True,}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Update Email-Id","required":True,}),
         "age":forms.NumberInput(attrs={"class":"form-control","placeholder":"Update Age","required":True,}),
		}

class NewUsrForm(forms.ModelForm):
	class Meta:
		model=NewData
		fields=['mobile','gender']
		widgets={
		"mobile":forms.TextInput(attrs={"class":"form-control","placeholder":"Update Mobile Number","max":10}),
		"gender":forms.Select(attrs={"class":"form-control",})
		}
			

