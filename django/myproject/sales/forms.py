from django import forms
from django.contrib.auth.models import User
from .models import GasSale, Employee

class EmployeeRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ['full_name', 'phone_number']

    def save(self, commit=True):
        user = User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        employee = super().save(commit=False)
        employee.user = user
        if commit:
            user.save()
            employee.save()
        return employee

class GasSaleForm(forms.ModelForm):
    class Meta:
        model = GasSale
        fields = ['cylinders_sold', 'total_amount']
