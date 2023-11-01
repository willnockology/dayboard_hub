from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Company, Yacht  # Import the custom User model

class UserForm(forms.ModelForm):
    class Meta:
        model = User  # This will now refer to your custom User model
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'user_type',
            'company',
            'yacht',
            'groups',
            'users_permissions',
            'uploaded_file',
            'uploaded_image',
        ]

    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already taken.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already taken.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class YachtForm(forms.ModelForm):
    class Meta:
        model = Yacht
        fields = ['name', 'length', 'width', 'draft', 'year_built', 'description']
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
