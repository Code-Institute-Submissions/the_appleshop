from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Review
from .forms import ReviewForm
from django.utils import timezone



def get_reviews(request):
    """
    Create a view that will return a list
    of Reviews that were published prior to 'now'
    and render them to the 'blogposts.html' template
    """
    reviews = Review.objects.filter(created_date__lte=timezone.now()
        ).order_by('-created_date')
    return render(request, "reviews.html", {'reviews': reviews})


def review_detail(request, id):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    review = get_object_or_404(Post, pk=id)
    review.views += 1
    review.save()
    return render(request, "reviewdetail.html", {'review': review})


def create_or_edit_review(request, id=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    review = get_object_or_404(Post, pk=id) if id else None
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect(review_detail, review.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'editform.html', {'form': form})


def delete_review(request, id):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    review = get_object_or_404(Post, pk=id)
    review.delete()
    review.save()
    return redirect(reverse('get_reviews'))