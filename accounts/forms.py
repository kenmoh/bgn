from django import forms
from django.core.exceptions import ValidationError
from .models import User, Education, BackgroundAdmin
from .states import STATE_CHOICES
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control-sm ', 'Placeholder': 'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control-sm ', 'Placeholder': 'Last Name'}))
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control-sm ', 'Placeholder': 'Username'}))
    phone = forms.CharField(label='', widget=forms.NumberInput(
        attrs={'class': 'form-control-sm ', 'Placeholder': 'Phone Number'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'form-control-sm ', 'Placeholder': 'Email'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control-sm ', 'Placeholder': 'Password', 'label': ''}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control-sm ', 'Placeholder': 'Confirm Password', 'label': ''}))

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'phone',
                  'email',
                  'password1',
                  'password2',
                  ]

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if User.objects.filter(phone=phone).exists():
            raise ValidationError('A user with that Phone already exists.')
        return phone

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('A user with that Email already exists.')
        return email


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'First Name'}))
    last_name = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Last Name'}))
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Username'}))
    phone = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Phone Number'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Email'}))
    location = forms.ChoiceField(label='', choices=STATE_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control-sm '}))
    skills = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Skills'}))
    about_me = forms.CharField(label='', required=True, widget=forms.Textarea(
        attrs={'rows': 2, 'class': 'form-control-sm', 'Placeholder': 'About Me'}))
    profile_image = forms.FileField(label='Profile Image')

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'phone',
                  'email',
                  'location',
                  'skills',
                  'about_me',
                  'profile_image'
                  ]


class ApplicationForm(forms.ModelForm):
    first_name = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'First Name'}))
    last_name = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Last Name'}))
    phone = forms.CharField(label='', widget=forms.NumberInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Phone Number'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Email'}))
    location = forms.ChoiceField(label='', choices=STATE_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control-sm '}))
    confirm = forms.BooleanField(label='Confirm')

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'phone',
                  'email',
                  'location',
                  'confirm'
                  ]


class EducationForm(forms.ModelForm):
    school = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'School'}))
    field_of_study = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Field of Study'}))
    qualification = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Qualification'}))
    year = forms.CharField(label='', widget=forms.DateInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Year'}))

    class Meta:
        model = Education
        fields = ['school',
                  'field_of_study',
                  'qualification',
                  'year',
                  ]


class BackgroundForm(forms.ModelForm):
    login_background = forms.FileField()
    register_background = forms.FileField()
    home_background = forms.FileField()

    class Meta:
        model = BackgroundAdmin
        fields = [
            'login_background',
            'register_background',
            'home_background'
        ]
