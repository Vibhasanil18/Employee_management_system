from django import forms
from .models import User, Department, Role

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'password', 'email', 'mobile',
            'dept', 'role', 'reporting_manager', 'date_of_joining',
        ]
        widgets = {
            'password': forms.PasswordInput(),
            'date_of_joining': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # Populate the dropdowns with data from the database
        self.fields['dept'].queryset = Department.objects.all()
        self.fields['role'].queryset = Role.objects.all()
        self.fields['reporting_manager'].queryset = User.objects.all()
