from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
import requests

FLASK_API_BASE = 'http://127.0.0.1:5000'

def signup(request):
    if request.method == 'POST':
        payload = {
            "company_name": request.POST.get("company_name"),
            "email": request.POST.get("email"),
            "password": request.POST.get("password"),
            "phone_number": request.POST.get("phone_number"),
            "username": request.POST.get("username"),
            "country": request.POST.get("country"),
            "state": request.POST.get("state"),
        }
        response = requests.post(f"{FLASK_API_BASE}/register", json=payload)
        if response.status_code == 201:
            return redirect('login')  # Redirect to login if registration is successful
        return JsonResponse(response.json(), status=response.status_code)

    # ✅ Add this for GET request
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            response = requests.post(f"{FLASK_API_BASE}/login", json={
                "email": email,
                "password": password
            })

            try:
                data = response.json()
            except ValueError:
                return JsonResponse({'message': 'Invalid response from server'}, status=500)

            if response.status_code == 200:
                request.session['user_id'] = data['user_id']
                request.session['username'] = data['username']
                request.session['is_authenticated'] = True
                # ✅ Do NOT try to fetch Django user
                return redirect('home')
            else:
                return JsonResponse(data, status=response.status_code)

        except requests.exceptions.RequestException as e:
            return JsonResponse({'message': f'Request failed: {e}'}, status=500)

    return render(request, 'login.html')


# Manually check for user authentication
def check_user_authentication(request):
    if 'user_id' in request.session:
        try:
            request.user = User.objects.get(id=request.session['user_id'])
        except User.DoesNotExist:
            request.user = None
            
# def signup(request):
#     if request.method == "POST":
#         company_name = request.POST.get("company_name")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         phone_number = request.POST.get("phone_number")
#         username = request.POST.get("username")
#         country = request.POST.get("country")
#         state = request.POST.get("state")
#         is_admin = request.POST.get("is_admin") == "on"  # Checkbox handling

#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already taken.")
#             return redirect('signup')

#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email already in use.")
#             return redirect('signup')

#         # Create user
#         user = User.objects.create_user(username=username, email=email, password=password)
#         user.first_name = company_name  # You can use first_name to store the company name
#         user.is_staff = is_admin  # Set admin status if selected
#         user.save()

#         messages.success(request, "Account created successfully! You can log in now.")
#         return redirect('login')

#     return render(request, "signup.html")


# def login_view(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")

#         try:
#             user = User.objects.get(email=email)  # Django auth uses username, so get the user first
#             user = authenticate(request, username=user.username, password=password)

#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # Redirect to a dashboard or home page
#             else:
#                 messages.error(request, "Invalid email or password.")
#         except User.DoesNotExist:
#             messages.error(request, "No user found with this email.")

#     return render(request, "login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')
