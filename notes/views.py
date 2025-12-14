from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from django.http import HttpResponseForbidden
from django.db.models import Q
# Create your views here.

@login_required
def note_list(request):
    query = request.GET.get('q')
    
       
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        attachment = request.FILES.get('attachment')

        if title and body:
            Note.objects.create(
                owner=request.user,
                title=title,
                body=body,
                attachment=attachment
            )
        return redirect('note_list')

    notes = Note.objects.filter(owner=request.user)
   #   this  is the searching logic here 
    if query:
       notes = Note.objects.filter(
          Q(title__icontains = query) |
          Q(body__icontains = query)
       )

    return render(request, 'notes/note_list.html', {'notes': notes,
    'query':query,})

@login_required
def note_edit(request,id):
 note = get_object_or_404(Note,id=id)
 if request.method == 'POST':
    note.title = request.POST.get('title')
    note.body = request.POST.get('body')

    if "attachment" in request.FILES:
       note.attachment = request.FILES.get('attachment')
    if note.owner != request.user:
       return HttpResponseForbidden("YOU are not allowed to do so!!!!")
    note.save()
    return redirect('note_list')

 return render(request,'notes/edit_notes.html',{'note':note})
     

def note_delete(request,id):
  note = get_object_or_404(Note, id = id)
  if  request.method == 'POST':
     if note.owner != request.user:
        HttpResponseForbidden("YOU are Not allowed to delete  the Note!!")
     note.delete()
     return redirect('note_list')
  return render(request,'notes/delete_note.html',{'note':note})

 
