"""
Main URL configuration for the Sticky Notes project.
"""
from django.contrib import admin  
from django.contrib.auth import views as auth_views  
from django.urls import include, path  
from django.shortcuts import redirect  

from notes.views import register_view

urlpatterns = [
    path('', lambda request: redirect('/notes/')),  
    
    path('admin/', admin.site.urls),
    
    # Registration route using our custom view.
    # yeh installed app "notes" ke andar views ko target kar raha hai 
    path('register/', register_view, name='register'),
    
    # Authentication routes using Django's built-in views.
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login',
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # App routes for all note-related pages.
    path('notes/', include('notes.urls')),
]