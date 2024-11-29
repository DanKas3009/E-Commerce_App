from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

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

def register_view(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'customer/register.html', {
                'error': "Passwords do not match"
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'customer/register.html', {
                'error': "Username already exists"
            })

        # Create user manually
        user = User(fname=fname, email=email, password=password1)
        user.save()
        return redirect('login/')

    return render(request, 'customer/register.html')