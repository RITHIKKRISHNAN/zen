
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('Client', 'Client'),
        ('Freelancer', 'Freelancer'),
        ('ProjectManager', 'Project Manager'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    bio = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    rating = models.FloatField(default=0.0)

class Project(models.Model):
    STATUS_CHOICES=[
        ('Pending','Pending'),
        ('Ongoing','Ongoing'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_projects')
    project_manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='managed_projects')
    freelancer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='freelancer_projects')
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')])

class Task(models.Model):
    STATUS_CHOICES=[
        ('Pending','Pending'),
        ('In Progress','In Progress'),
        ('Completed','Completed'),
        ('Rejected','Rejected'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Rejected', 'Rejected')])
    due_date = models.DateField()

class Invoice(models.Model):
    STATUS_CHOICES=[
        ('Unpaid','Unpaid'),
        ('Paid','Paid'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='invoices')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid')])