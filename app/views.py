from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

# Add Employee
def add_employee(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard after saving
    else:
        form = UserForm()  # Initialize empty form
    return render(request, 'add_employee.html', {'form': form})

# Update Employee
def update_employee(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard after updating
    else:
        form = UserForm(instance=user)
    return render(request, 'update_employee.html', {'form': form, 'user': user})

# Delete Employee
def delete_employee(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('dashboard')  # Redirect to the dashboard after deletion

# Dashboard
def dashboard(request):
    employees = User.objects.all()
    return render(request, 'dashboard.html', {'employees': employees})
