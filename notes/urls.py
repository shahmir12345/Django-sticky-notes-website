"""
URL patterns for note-related pages.
"""
from django.urls import path

from . import views

# from .views import custom_logout

# yeh is App ke saaray views ko access kar sakta hai , but isko hum ne main urls.py main include kar diya hai so kisi bhi url pe easily ja saktay hain

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('new/', views.note_create, name='note_create'),
    path('<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('<int:pk>/delete/', views.note_delete, name='note_delete'),
    # path('logout/', custom_logout, name='logout'), yawr yeh yahan main ne URL add kiya tha, admin jab logout karay tu admin login page par nhi balkay User ke login page par aata hai  
]
