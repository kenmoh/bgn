from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Post, Event, About, Objective, Executive
from accounts.models import User, Application
from .forms import PostForm


def index(request):
    about = About.objects.all()
    applications = Application.objects.all()
    context = {
        'about': about,
        'applications': applications
    }
    return render(request, 'pages/index.html', context)


def blog(request):
    blogs = Post.objects.all().order_by('-date_posted')
    context = {
        'blogs': blogs,
    }
    return render(request, 'pages/blog.html', context)


def blog_detail(request, id):
    blog = get_object_or_404(Post, pk=id)
    context = {
        'blog': blog
    }
    return render(request, 'pages/blog_detail.html', context)


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


def contact(request):
    return render(request, 'pages/contact.html')


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
