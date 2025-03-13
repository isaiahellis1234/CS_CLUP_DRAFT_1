from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from .forms import PostForm, CommentForm
from .models import Post

def frontpage(request):
    posts = Post.objects.all()  # Fetch all posts

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            # Create an instance but don't save to the database yet
            post = form.save(commit=False)

            # Generate a slug from the title
            post.slug = slugify(post.title)

            # Ensure the slug is unique by checking if it already exists in the database
            original_slug = post.slug
            counter = 1
            while Post.objects.filter(slug=post.slug).exists():
                post.slug = f"{original_slug}-{counter}"
                counter += 1

            # Save the post to the database
            post.save()

            # Redirect to the frontpage view
            return redirect("frontpage")

    else:
        form = PostForm()

    return render(request, "blog/frontpage.html", {"posts": posts, "form": form})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)  # Get the post by its slug

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # Associate the comment with the post
            comment.save()
            return redirect('post_detail', slug=post.slug)  # Redirect to avoid resubmission
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})