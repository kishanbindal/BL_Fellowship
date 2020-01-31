from django.urls import path, include
from . import views


urlpatterns = [
    path('api/notes/', views.NoteView.as_view(), name='notes'),
    path('api/notes/<id>', views.NoteOperationsView.as_view(), name='notes-op'),
    path('api/labels/', views.LabelView.as_view(), name='labels'),
    path('api/labels/<id>', views.LabelOperationsView.as_view(), name='labels-op'),
    path('api/archived', views.ViewArchivedNotes.as_view(), name='archived-notes'),
    path('api/trashed', views.ViewTrashedNotes.as_view(), name='trashed-notes'),
    path('api/search', views.SearchNote.as_view(), name='search')
]
