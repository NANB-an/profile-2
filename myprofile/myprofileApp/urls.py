from django.urls import path
from .views_login import login_view, logout_view, register_view
from .views_profile import profile_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    
]
