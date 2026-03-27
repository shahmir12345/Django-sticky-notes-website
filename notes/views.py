"""
Views for the Sticky Notes app.
"""
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note

# from django.shortcuts import redirect
# from django.contrib.auth import logout


@login_required
def note_list(request):
    """
    Show only the notes that belong to the logged-in user.
    """
    notes = Note.objects.filter(owner=request.user)
    return render(request, 'notes/note_list.html', {'notes': notes})


@login_required
def note_create(request):
    """
    Create a new note and automatically attach the current user as owner.
    """
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user  # Owner should never come from user input.
            note.save()
            messages.success(request, 'Note created successfully.')
            return redirect('note_list')
    else:
        form = NoteForm()

    return render(request, 'notes/note_form.html', {
        'form': form,
        'page_title': 'Create Note',
        'button_text': 'Save Note',
    })


@login_required
def note_edit(request, pk):
    """
    Edit an existing note.
    get_object_or_404 ensures the user can only edit their own note aur agar yeh nhi hua tu yeh 404 ka error de dega.
    """
    note = get_object_or_404(Note, pk=pk, owner=request.user)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated successfully.')
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/note_form.html', {
        'form': form,
        'page_title': 'Edit Note',
        'button_text': 'Update Note',
    })


@login_required
def note_delete(request, pk):
    """
    Ask for confirmation before deleting a note.
    Users can only delete their own notes.
    """
    note = get_object_or_404(Note, pk=pk, owner=request.user)

    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note deleted successfully.')
        return redirect('note_list')

    return render(request, 'notes/note_confirm_delete.html', {'note': note})


def register_view(request):
    """
    Register a new user using Django's built-in UserCreationForm.
    After successful registration, log the user in and redirect to /notes/.
    """
    if request.user.is_authenticated:
        return redirect('note_list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. Welcome!')
            return redirect('note_list')
    else:
        form = UserCreationForm()

    return render(request, 'notes/register.html', {'form': form})


#  yawr yeh yahan main ne URL add kiya tha, admin jab logout karay tu admin login page par nhi balkay User ke login page par aata hai  

# def custom_logout(request):
#     logout(request)  # Logout current user

#     if request.user.is_superuser:
#         return redirect('/admin/login/')  # Admin ko admin login page pe redirect karo
#     else:
#         return redirect('/login/')  # Normal user ko user login page pe redirect karo