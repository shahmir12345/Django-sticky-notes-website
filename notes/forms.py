"""
Forms used in the Sticky Notes app.
"""
from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    """
    ModelForm for creating and editing notes.
    Only title, content, and color are exposed to the user.
    """

    class Meta:
        model = Note
        fields = ['title', 'content', 'color']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter note title',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Write your note here...',
            }),
            # Color input gives a nicer UX while still storing a hex value.
            'color': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'color',
            }),
        }
