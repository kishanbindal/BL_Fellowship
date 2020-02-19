from django.db import models
from Fun.models import User


class Label(models.Model):
    label_name = models.CharField(max_length=64, blank=True)
    user = models.ForeignKey(User, related_name='LabelUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.label_name


class Note(models.Model):

    user = models.ForeignKey(User, related_name='NoteUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=64, blank=True)
    note_text = models.TextField(blank=True)
    note_image = models.ImageField(upload_to='images/', blank=True, null=True)
    labels = models.ManyToManyField(Label, blank=True)
    collaborators = models.ManyToManyField(User, blank=True)
    is_archived = models.BooleanField(default=False)
    is_trashed = models.BooleanField(default=False)
    color = models.CharField(max_length=16, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    is_pinned = models.BooleanField(default=False)
    link = models.URLField(blank=True, null=True)
    reminder = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
