from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Post, Comment, Like
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            if form.cleaned_data.get("is_club_admin"):
                user.is_active = False   # ⬅ deactivate account
                user.is_club_admin = True
            else:
                user.is_club_admin = False

            user.save()

            # Only auto login normal users
            if user.is_active:
                login(request, user)
                return redirect("home")
            else:
                return redirect("approval_pending")

    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

@login_required
def home(request):
    posts = Post.objects.all().order_by('-created')
    club_admins = User.objects.filter(is_club_admin=True)
    total_posts = Post.objects.count()
    total_admins = club_admins.count()
    total_likes = sum(post.likes.count() for post in posts)

    return render(request,'home.html',{'posts':posts, 'club_admins': club_admins, 'total_posts': total_posts, 'total_admins': total_admins, 'total_likes': total_likes,})

@login_required
def create_post(request):

    if not request.user.is_club_admin:
        return render(request, "not_allowed.html")

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("home")
    else:
        form = PostForm()

    return render(request, "create_post.html", {"form": form})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    like, created = Like.objects.get_or_create(
        post=post,
        user=request.user
    )

    if not created:
        like.delete()

    return redirect('home')

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post,id=post_id)

    if request.method == "POST":
        text = request.POST.get("text")
        Comment.objects.create(
            post=post,
            user=request.user,
            text=text
        )

    return redirect('home')

def club_admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_club_admin and not request.user.is_approved:
            return HttpResponse("Waiting for admin approval")
        return view_func(request, *args, **kwargs)
    return wrapper

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)

    # Only allow viewing club admin profiles
    if not user.is_club_admin:
        return redirect("home")

    posts = Post.objects.filter(user=user).order_by("-created")
    total_likes = sum(post.likes.count() for post in posts)
    return render(request, "profile.html", {
        "profile_user": user,
        "posts": posts,
        "total_likes": total_likes
    })

def approval_pending(request):
    return render(request, "approval_pending.html")