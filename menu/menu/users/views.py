from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerRegister

def register(request):
    if request.method == 'POST':
        form = CustomerRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(f"{username} created successfully")
            messages.success(request, f'Account created for {username}!')
        else:
            print(form.errors)
        return redirect('restaurant-home')
    else:
        form = CustomerRegister()
        
    return render(request, 'users/register.html', {'form': form})    


# Create your views here.
