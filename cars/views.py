# cars/views.py
from django.shortcuts import render

def index(request):
    # Your view logic goes here
    return render(request, 'cars/index.html')  # Replace 'cars/index.html' with your template path

# cars/views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'cars/login.html'  # Create a login template
    success_url = reverse_lazy('home')  # Replace 'home' with your home page URL name

class CustomLogoutView(LogoutView):
    pass  # You can customize the logout behavior if needed
