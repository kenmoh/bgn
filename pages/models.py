from django.db import models
from accounts.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=125)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user}'

    def total_likes(self):
        return self.likes.count()


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=125)
    content = models.TextField()
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    video = models.FileField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user}'


class About(models.Model):
    heading = models.CharField(max_length=125)
    content = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    vision = models.TextField(null=True, blank=True)
    mission = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.heading


class Objective(models.Model):
    objective = models.TextField()

    def __str__(self):
        return self.objective


class Executive(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    position = models.CharField(max_length=75)
    about_me = models.CharField(max_length=75)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    place_of_work = models.CharField(max_length=125)
    subject = models.CharField(max_length=125)
    message = models.TextField()

    def __str__(self):
        return f'{self.name}'

