from rest_framework import serializers
from .models import Label, Note


class CreateNoteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Note
        fields = ['title', 'note_text']
