from django.urls  import path
from  . import views

urlpatterns = [
    path("",views.note_list, name='note_list'),
    path('edit/<int:id>/', views.note_edit, name = 'note-edit'),
    path('delete/<int:id>/',views.note_delete, name = 'note-delete'),
]
