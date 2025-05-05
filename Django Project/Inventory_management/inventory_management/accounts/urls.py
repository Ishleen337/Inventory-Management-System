from django.urls import path
from .views import register_user, login_user, dashboard, logout_user
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    # path('', home, name="home"),
    # path('protected/', views.protected_view, name='protected'),
    path('logout/', views.logout_view, name='logout'),
]
