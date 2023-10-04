from django.http import HttpResponse
from django.shortcuts import render, redirect

from vendor.forms import VendorForm
from .forms import Userform
from .models import User, UserProfile
from django.contrib import messages


# Create your views here.
def registerUser(request):  # method ta ki????       #method ta form a rakhbo        #rakhar por form ki valid
    # #then
    # save and redirect
    if request.method == 'POST':
        print(request.POST)
        form = Userform(request.POST)
        if form.is_valid():
            # Create User using Form
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.CUSTOMER
            user.save()

            # Create User using create_user model first_name = form.cleaned_data['first_name'] last_name =
            # form.cleaned_data['last_name'] username = form.cleaned_data['username'] email = form.cleaned_data[
            # 'email'] password = form.cleaned_data['password'] user = User.objects.create_user(
            # first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            # user.role = User.CUSTOMER user.save() print("User is created through create_user model")
            messages.success(request, "Your account has been created successfully!!")
            return redirect('registerUser')
        else:
            print(form.errors)
    else:
        form = Userform()
    context = {
        'form': form,
    }
    return render(request, 'accounts/registerUser.html', context)


def registerVendor(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        v_form = VendorForm(request.POST, request.FILES)
        if form.is_valid() and v_form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.VENDOR
            user.save()
            vendor = v_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            print("User is created through create_user model")
            messages.success(request, "Your account has been created successfully.Please wait for the approval")
            return redirect('registerUser')
        else:
            print(form.errors)
    else:
        form = Userform()
        v_form = VendorForm()

    context = {
        'form': form,
        'v_form': v_form,
    }
    return render(request, 'accounts/registerVendor.html', context)
