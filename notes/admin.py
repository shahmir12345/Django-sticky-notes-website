"""
Admin configuration for the notes app.
hum apnay model Ko admin par bhi show karwa saktay hain jo DJANGO ka apna hai 
isi liye hum ne yahan Model ko import kia hua hai
"""
from django.contrib import admin

from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """Admin panel customization for Note objects."""
    list_display = ('title', 'owner', 'color', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'owner__username')
    list_filter = ('color', 'created_at', 'updated_at')
