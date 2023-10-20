from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Company(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(AbstractUser):
    user_type_choices = (
        ('superuser', 'SuperUser'),
        ('yacht_manager', 'Yacht Manager'),
        ('yacht_admin', 'Yacht Admin'),
        ('captain', 'Captain'),
        ('crew', 'Crew'),
    )
    user_type = models.CharField(max_length=20, choices=user_type_choices)
    
    # Define a ForeignKey to Company with a default value for superusers, yacht managers, and yacht admins
    company = models.ForeignKey(
        Company, 
        on_delete=models.SET_DEFAULT, 
        default=1,  # Assuming "Dayboard" has an ID of 1
    )

    yacht = models.ForeignKey('Yacht', on_delete=models.SET_NULL, null=True, blank=True)
    groups = models.ManyToManyField(Group, blank=True, related_name="custom_user_set")
    users_permissions = models.ManyToManyField(Permission, blank=True, related_name="custom_user_set")
    uploaded_file = models.FileField(upload_to='files', null=True, blank=True)
    uploaded_image = models.ImageField(upload_to='images', null=True, blank=True)

class Yacht(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=255)
    yacht = models.ForeignKey(Yacht, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Form(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    yacht = models.ForeignKey(Yacht, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    submission_time = models.DateTimeField()
    update_time = models.DateTimeField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_file = models.FileField(upload_to='files', null=True, blank=True)
    uploaded_image = models.ImageField(upload_to='images', null=True, blank=True)

class FormField(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    yacht = models.ForeignKey(Yacht, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_file = models.FileField(upload_to='files', null=True, blank=True)
    uploaded_image = models.ImageField(upload_to='images', null=True, blank=True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    status = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
