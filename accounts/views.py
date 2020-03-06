from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Experience, Education, User, BackgroundAdmin, Success
from .forms import RegistrationForm, UserUpdateForm, ApplicationForm
from pages .models import Post


# REGISTRATION

def register(request):
    """User Registration """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Account created Successfully ! You can now Login')
            return redirect('login')

    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def change_user(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST or None, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'User Updated Successfully !')
            if request.user.is_employer:
                return redirect('employer-dashboard', request.user.id)
            else:
                return redirect('dashboard', request.user.id)
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'form': form
    }

    return render(request, 'accounts/update.html', context)


# LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        # Check if user is in database
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in !')
            return redirect('dashboard', request.user.pk)
        else:
            messages.error(request, 'Invalid Credentials, Check username or password')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html', {'background': BackgroundAdmin})


def logout_view(request):
    logout(request)
    return redirect('index')


# DELETE USER
def delete_user(request, id):
    user = User.objects.all().get(pk=id)
    user.delete()
    messages.success(request, f'Account with {user.username} deleted successfully')
    return redirect('index')


# ADD EDUCATION
def add_education(request):
    """ Add Education """
    if request.method == 'POST':
        # Get form Values
        user_id = request.POST['user_id']
        school = request.POST['school']
        field_of_study = request.POST['field_of_study']
        qualification = request.POST['qualification']
        year = request.POST['year']

        education = Education(user_id=user_id, school=school, field_of_study=field_of_study,
                              qualification=qualification, year=year)
        education.save()

        messages.success(request, 'Eduction added successfully.')
        return redirect('dashboard', request.user.pk)
    else:
        return render(request, 'accounts/education.html')


# EDIT EDUCATION
def edit_education(request, id):
    """ This view is to edit user education"""
    education = Education.objects.get(pk=id)
    context = {
        'education': education
    }
    if request.method == 'POST':
        education.user_id = request.POST['user_id' or None]
        education.school = request.POST['school' or None]
        education.field_of_study = request.POST['field_of_study' or None]
        education.qualification = request.POST['qualification' or None]
        education.year = request.POST['year' or None]

        education.save()
        messages.success(request, 'Education Updated Successfully, you may add another !')
        return redirect('dashboard', request.user.pk)
    else:
        return render(request, 'accounts/edit_education.html', context)

    # DELETE EDUCATION


def delete_edu(request, id):
    education = Education.objects.all().get(pk=id)
    education.delete()
    messages.success(request, f'Education successfully deleted')
    return redirect('index')


def add_experience(request):
    """ Add Experience """
    if request.method == 'POST':
        # Get form values
        user_id = request.POST['user_id']
        company_name = request.POST['company_name']
        job_title = request.POST['job_title']
        year_from = request.POST['year_from']
        year_to = request.POST['year_to']
        job_description = request.POST['job_description']

        experience = Experience(user_id=user_id, company_name=company_name, job_title=job_title,
                                year_from=year_from, year_to=year_to, job_description=job_description)
        experience.save()

        messages.success(request, 'Experience added successfully. You may add more')
        return redirect('dashboard', request.user.pk)
    else:
        return render(request, 'accounts/experience.html')


# EDIT EXPERIENCE
def edit_experience(request, id):
    """ This view is to edit user experience """
    experience = Experience.objects.get(pk=id)
    context = {
        'experience': experience
    }
    if request.method == 'POST':
        experience.user_id = request.POST['user_id' or None]
        experience.company_name = request.POST['company_name' or None]
        experience.job_title = request.POST['job_title' or None]
        experience.job_description = request.POST['job_description' or None]
        experience.year_from = request.POST['year_from' or None]
        experience.year_to = request.POST['year_to' or None]

        experience.save()
        messages.success(request, 'Experience Updated Successfully')
        return redirect('dashboard', request.user.pk)
    else:
        return render(request, 'accounts/edit_experience.html', context)


# DELETE EXPERIENCE
def delete_exp(request, id):
    experience = Experience.objects.all().get(pk=id)
    experience.delete()
    messages.success(request, 'Experience successfully deleted')
    return redirect('dashboard', experience.user_id)

@login_required
def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST or None, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Application Successful !')
            return redirect('dashboard', request.user.pk)
    else:
        form = ApplicationForm(instance=request.user)
    return render(request, 'accounts/apply.html', {'form': form})


def update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES or None, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'User Updated Successfully !')
            # return redirect('dashboard', request.user.id)
            return redirect('dashboard', request.user.pk)
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'form': form
    }

    return render(request, 'accounts/update.html', context)


def profile(request, id):
    user = get_object_or_404(User, pk=id)
    educations = Education.objects.all().filter(user=user)
    experiences = Experience.objects.all().filter(user=user)
    context = {
        'user': user,
        'educations': educations,
        'experiences': experiences
    }
    return render(request, 'accounts/profile.html', context)


def dashboard(request, id):
    user = get_object_or_404(User, pk=id)
    posts = Post.objects.all().filter(user=user).order_by('-date_posted')
    experiences = Experience.objects.all().filter(user=user)
    educations = Education.objects.all().filter(user=user)
    successes = Success.objects.all()
    context = {
        'user': user,
        'posts': posts,
        'experiences': experiences,
        'educations': educations,
        'successes': successes
    }
    return render(request, 'accounts/dashboard.html', context)
