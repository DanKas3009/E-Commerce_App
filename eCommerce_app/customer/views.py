from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log the user in
            return redirect('home/')  # Replace 'home' with your desired URL
    else:
        form = AuthenticationForm()
    return render(request, 'customer/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            # Log the user in after registration
            return redirect('login/')
    else:
        form = UserCreationForm()
    return render(request, 'customer/register.html', {'form': form})