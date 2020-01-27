from rest_framework import serializers
from .models import Label, Note


class CreateNoteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Note
        # fields = ['title', 'note_text', 'note_image', 'labels', 'collaborators', 'is_archived']
        exclude = ['user', ]
        # fields = '__all__'


class NoteOperationsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Note
        fields = ['title', 'note_text', 'note_image', 'labels', 'collaborators', 'is_archived', 'is_trashed', 'color',
                  'is_pinned', 'link', 'reminder']


class CreateLabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        exclude = ['user', ]


class LabelOperationsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Label
        fields = ['label_name']
