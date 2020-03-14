from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Post, Event, About, Objective, Executive, Contact
from accounts.models import User, Application, BackgroundAdmin, Sponsor
from .forms import PostForm
from django.template.loader import render_to_string
from django.http import JsonResponse


def index(request):
    about = About.objects.all()
    applications = Application.objects.all()
    backgrounds = BackgroundAdmin.objects.all()
    sponsors = Sponsor.objects.all()
    events = Event.objects.all()
    context = {
        'about': about,
        'applications': applications,
        'backgrounds': backgrounds,
        'sponsors': sponsors,
        'events': events
    }
    return render(request, 'pages/index.html', context)


def blog(request):
    blogs = Post.objects.all().order_by('-date_posted')
    context = {
        'blogs': blogs,
    }
    return render(request, 'pages/blog.html', context)


@login_required
def blog_detail(request, id):
    blog = get_object_or_404(Post, pk=id)
    is_liked = False
    if blog.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {
        'blog': blog,
        'is_liked': is_liked
    }
    return render(request, 'pages/blog_detail.html', context)


@login_required
def likes(request):
    blog = get_object_or_404(Post, id=request.POST['blog_id'])
    is_liked = False
    if blog.likes.filter(id=request.user.id).exists():
        blog.likes.remove(request.user)
        is_liked = False
    else:
        blog.likes.add(request.user)
        is_liked = True
    context = {
        'blog': blog,
        'is_liked': is_liked
    }
    if request.is_ajax():
        html = render_to_string('partials/_likes.html', context, request=request)
        return JsonResponse({'form': html})


def post(request):
    """User Registration """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post_form = form.save(commit=False)
            post_form.user = request.user
            post_form.save()
            messages.success(
                request, f'Blog created Successfully !')
            return redirect('blog')

    else:
        form = PostForm()
    return render(request, 'pages/post.html', {'form': form})


# Edit Blog
def edit_blog(request, id):
    blog = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=blog)
        if form.is_valid():
            edited_form = form.save(commit=False)
            edited_form.user = request.user
            edited_form.save()
            messages.success(request, 'Blog Updated Successfully')
            return redirect('dashboard', request.user.pk)
        else:
            context = {
                'form': form
            }
            return render(request, 'employers/post.html', context)
    else:
        context = {
                'form': PostForm(instance=blog)
            }
        return render(request, 'pages/post.html', context)


# Delete Blog
def delete_blog(request, id):
    post = Post.objects.all().get(pk=id)
    post.delete()
    messages.success(request, 'Blog successfully deleted')
    return redirect('dashboard', post.user_id)


def event(request):
    events = Event.objects.all().order_by('-id')
    context = {
        'events': events
    }
    return render(request, 'pages/events.html', context)


def about(request):
    about = About.objects.all()
    objectives = Objective.objects.all()
    executives = Executive.objects.all()
    context = {
        'about': about,
        'objectives': objectives,
        'executives': executives,
    }
    return render(request, 'pages/about.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        place_of_work = request.POST['place_of_work']
        subject = request.POST['subject']
        message = request.POST['message']

        new_contact = Contact(name=name, email=email, place_of_work=place_of_work, subject=subject, message=message)
        new_contact.save()
        messages.success(request, 'Thank you for contacting us, we will get back to you shortly !')

        return redirect('contact')
    else:
        return render(request, 'pages/contact.html')

