from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm, UserAddressForm, UserAddress


@login_required
def logout(request):
    """ Logs the user out """
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect(reverse('index'))

def login(request):
    """ Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('profile'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!" )
                return redirect(reverse('profile'))
            else:
                login_form.add_error(None, "Your username and password is incorrect")

    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})

def registration(request):
    """ Render the registration page """
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered.")
                return redirect(reverse('profile'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})

def user_profile(request):
    """ The user's profile page """
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    else:
        try:
            user_address = UserAddress.objects.get(user=request.user.id)
            address='yes'
            user_addressform=UserAddressForm(instance=user_address)
            messages.success(request, "This is your current Shipping Address.")

        except:
            user_addressform=UserAddressForm()
            address='no'
            messages.success(request, "Shipping Address not found.")

        if request.method == "POST":
            user_addressform = UserAddressForm(request.POST)
            if user_addressform.is_valid:
                user_address = user_addressform.save(commit=False)
                user_address.user=request.user
                user_address.save()
            messages.success(request, "Shipping Address updated.")
            address='updated'
    
    return render(request, 'profile.html', {'user_addressform': user_addressform, 'address': address})