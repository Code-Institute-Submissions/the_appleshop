from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Review
from .forms import ReviewForm
from django.utils import timezone
from django.contrib import messages


def get_reviews(request, id=None):
    """
    Creates view with overview of entered reviews prior to 'now'
    """
    if id is not None:
        reviews = Review.objects.filter(pk=id).order_by('-created_date')
    else:
        reviews = Review.objects.filter(created_date__lte=timezone.now()
            ).order_by('-created_date')
    return render(request, "reviews.html", {'reviews': reviews})


def review_detail(request, id):
    """
    Create a view that returns a single
    Review object based on the post ID (id) and
    render it to the 'reviewdetail.html' template.
    Or return a 404 error if the review is
    not found
    """
    review = get_object_or_404(Review, pk=id)
    print('review', type(review), review)
    review.view_count += 1
    review.save()
    return render(request, "reviewdetail.html", {'review': review})

def create_review(request, id=None):
    """
    Create a view that allows us to create
    or edit a review depending if the Review ID
    is null or not
    """
    review = get_object_or_404(Review, pk=id) if id else None

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect(review_detail, review.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'editform.html', {'form': form})



def create_or_edit_review(request, id=None):
    """
    Create a view that allows us to create
    or edit a review depending if the Review ID
    is null or not
    """
    review = get_object_or_404(Review, pk=id) if id else None

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
    View for deleting a review, requested by author
    """
    review = get_object_or_404(Review, pk=id)
    review.delete()
    review.save()
    messages.success(request, "Review has been deleted")
    return redirect(reverse('get_reviews'))