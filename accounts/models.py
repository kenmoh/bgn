from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from .states import STATE_CHOICES


class User(AbstractUser):
    """
    Custom User Model
    """
    phone = models.CharField(max_length=35, unique=True)
    skills = models.CharField(max_length=1050)
    about_me = models.TextField()
    location = models.CharField(max_length=35, choices=STATE_CHOICES)
    profile_image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_approved = models.BooleanField(default=False)
    confirm_application = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username}'

    def skills_as_list(self):
        # Split Skills with comma
        return self.skills.split(',')


class BackgroundAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    login_background = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    register_background = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    home_background = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return 'Background Image'

    class Meta:
        verbose_name_plural = 'Backgrounds'


class Education(models.Model):
    """ Education """

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    school = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.user}'


class Experience(models.Model):
    """ Experience """

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    year_from = models.IntegerField()
    year_to = models.IntegerField()
    job_description = models.TextField()

    def __str__(self):
        return f'{self.user}'


class Application(models.Model):
    title = models.CharField(max_length=75)
    message = models.CharField(max_length=75)

    def __str__(self):
        return self.title


class Success(models.Model):
    title = models.CharField(max_length=75)
    message = models.CharField(max_length=75)

    def __str__(self):
        return self.title
