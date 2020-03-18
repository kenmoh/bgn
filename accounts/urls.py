from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('dashboard/<int:id>', views.dashboard, name='dashboard'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('add_education', views.add_education, name='add_education'),
    path('edit_education/<int:id>', views.edit_education, name='edit_education'),
    path('delete_education/<int:id>', views.delete_edu, name='delete_education'),
    path('add_experience', views.add_experience, name='add_experience'),
    path('edit_experience/<int:id>', views.edit_experience, name='edit_experience'),
    path('delete_experience/<int:id>', views.delete_exp, name='delete_experience'),
    path('apply', views.apply, name='apply'),
    path('update', views.update, name='update'),
    path('delete/<int:id>', views.delete_user, name='delete'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('delete_msg/<int:id>', views.delete_msg, name='delete_msg'),
]

