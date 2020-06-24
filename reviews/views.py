from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Review
from django.contrib.auth.models import User
from products.models import Product
from .forms import ReviewForm
from django.utils import timezone
from django.contrib import messages


def get_reviews(request, pk=None):
    """
    Creates view with overview of entered reviews prior to 'now'
    """
    if pk is not None:
        reviews = Review.objects.filter(pk=pk).order_by('-created_date')
    else:
        reviews = Review.objects.filter(created_date__lte=timezone.now()
            ).order_by('-created_date')
    return render(request, "reviews.html", {'reviews': reviews})


def review_detail(request, pk):
    """
    Create a view that returns a single
    Review object based on the post ID (id) and
    render it to the 'reviewdetail.html' template.
    Or return a 404 error if the review is
    not found
    """
    review = get_object_or_404(Review, pk=pk)
    review.view_count += 1
    review.save()
    return render(request, "reviewdetail.html", {'review': review})


def create_review(request, pk):
    """
    Create a view that allows us to create
    or edit a review depending if the Review ID
    is null or not
    """
    product=Product.objects.get(pk=pk)
    review = Review(author=request.user, product=product)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author.id=request.user.id
            review.product.pk=pk
            review.save()
            return redirect(review_detail, review.pk)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'editform.html', {'form': form})



def edit_review(request, pk=None):
    """
    Create a view that allows us to create
    or edit a review depending if the Review ID
    is null or not
    """
    review = get_object_or_404(Review, pk=pk) if pk else None
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect(review_detail, review.pk)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'editform.html', {'form': form})


def delete_review(request, pk):
    """
    View for deleting a review, requested by author
    """
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    review.save()
    messages.success(request, "Review has been deleted")
    return redirect(reverse('get_reviews'))