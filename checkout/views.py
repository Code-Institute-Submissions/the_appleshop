from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe
from accounts.models import UserAddress
from accounts.forms import UserAddressForm


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

def update_ordered_pcs(request):
    cart = request.session.get('cart', {})
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        product.ordered_pcs+=quantity


@login_required()
def checkout(request):
    user_address_current = None
    try:
        user_address_current = UserAddress.objects.get(user=request.user.id)
        messages.success(request, "This is your current Shipping Address.")
        address='yes'
    except:
        messages.success(request, "No address found in database")

    if request.method=="POST":            
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order = order, 
                    product = product, 
                    quantity = quantity
                    )
                order_line_item.save()
                
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid")
                update_ordered_pcs(request)
                request.session['cart'] = {}
                try:
                    user_cart=Cart.objects.get(user=request.user.id)
                    user_cart.product_list = ""
                    user_cart.save()
                    user_address_new = user_addressform.save(commit=False)
                    user_address_new.user=request.user
                    user_address_new.pk = user_address_current.pk
                    user_address_new.save()  

                except:
                    return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        if user_address_current:
            order_form = OrderForm(instance=user_address_current)
        else:
            order_form = OrderForm()
        payment_form = MakePaymentForm()

        
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
                
            