"""
Models for the Sticky Notes app.
"""
from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    """
    Represents a single sticky note that belongs to one user.
    yahan par saari Fields Define hoti hain models.py
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    color = models.CharField(max_length=7, default='#FFFF99')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    class Meta:
        ordering = ['-updated_at']  # Latest updated notes appear first.

    def __str__(self):
        """String shown in admin and shell."""
        return self.title
