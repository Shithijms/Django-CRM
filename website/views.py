from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from .forms import SignUpForm, AddRecordForm
# Home View - Handles login
def home(request):
    records = Record.objects.all()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect('home')
    
    return render(request, 'home.html', {'records' :records})

# Logout View
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

# Register View
def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # Authenticate and login new user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully registered!")
                return redirect('home')
            else:
                messages.error(request, "Registration failed. Please try again.")

    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id = pk)
        return render(request,'record.html',{'customer_record' : customer_record})
    else:
        messages.success(request, "You must be logged in order to view")
        return redirect('home')
    
def delete_record(request, pk):
        if request.user.is_authenticated:
            delete_it = Record.objects.get(id = pk)
            delete_it.delete()
            messages.success(request, "Record Deleted Successfully!.")
            return redirect('home')
        else:
            messages.success(request, "You must be logged in order to delete")
            return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"Record added successfully!")
                return redirect('home')
        return render(request, 'add_record.html',{'form':form})
    
    else:
            messages.success(request, "You must be logged in order to register")
            return redirect('home')      

def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id = pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated!")
            return redirect('home')
        return render(request, 'update_record.html',{'form':form})
    else:
            messages.success(request, "You must be logged in order to register")
            return redirect('home')  