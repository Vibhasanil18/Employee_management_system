from django.db import models

# Department Model
class Department(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Role Model
class Role(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# User Model (Employee)
class User(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    reporting_manager = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    date_of_joining = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
