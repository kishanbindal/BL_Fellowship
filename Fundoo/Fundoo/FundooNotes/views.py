from django.http import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from Fun.models import User
from util.decorators import logged_in
from .models import Note, Label
from .serializers import CreateNoteSerializer, NoteOperationsSerializer, CreateLabelSerializer, \
    LabelOperationsSerializer
from Fundoo.redis_class import Redis
from services import TokenService

rdb = Redis()


class NoteView(GenericAPIView):

    queryset = Note.objects.all()
    serializer_class = CreateNoteSerializer

    def get(self, request, *args, **kwargs):

        try:

            notes = self.queryset.filter(is_archived=False, is_trashed=False)
            return Response(notes.values(), status=status.HTTP_200_OK)

        except Exception:

            return Response(Exception, status=status.HTTP_403_FORBIDDEN)

    def post(self, request, *args, **kwargs):

        smd = {
            'success': 'FAIL',
            'message': 'Failed To add Note to Server Database',
            'data': []
        }

        try:
            serializer = CreateNoteSerializer(data=request.data)

            if serializer.is_valid():
                # user = request.user
                serializer.save(user_id=41)
                smd['success'], smd['message'] = 'Success', 'Note Successfully created'
                return JsonResponse(data=smd, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(Exception, status=status.HTTP_403_FORBIDDEN)


class NoteOperationsView(GenericAPIView):

    queryset = Note.objects.all()
    serializer_class = NoteOperationsSerializer

    def get(self, request, id, *args, **kwargs):

        try:
            smd = {
                'success': 'FAIL',
                'message': f'Unsuccessful in retrieving note with id : {id}',
                'data': []
            }
            note = self.queryset.filter(pk=id)
            if note.values() is not None:
                smd = {
                    'success': 'Successful',
                    'message': f'Successfully retrieved note with id : {id}',
                    'data': [note.values()]
                }
                return Response(smd, status=status.HTTP_200_OK)
            else:
                return Response(smd, status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return Response(Exception, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, *args, **kwargs):

        try:
            smd = {
                'Success': 'Fail',
                'message': 'Unsuccessful in updating Note',
                'data': [],
            }
            serializer = NoteOperationsSerializer(data=request.data)

            if serializer.is_valid():

                note = Note.objects.get(pk=id)
                serializer.update(note, serializer.data)
                smd['Success'], smd['message'] = 'success', f'Successfully update Note with id: {id}'
                return Response(smd, status=status.HTTP_200_OK)
            else:
                smd['data'] = [serializer.errors]
                return Response(smd, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(Exception, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id, *args, **kwargs):

        smd = {
            'Success': 'Fail',
            'message': 'Deletion of Note Unsuccessful',
            'data': []
        }
        note = self.queryset.get(pk=id)
        if note is not None:
            print(note.delete())
            smd['Success'], smd['message'] = 'Success', 'Deletion of Note unsuccessful'
            return Response(data=smd, status=status.HTTP_200_OK)
        else:
            return Response(smd, status=status.HTTP_400_BAD_REQUEST)


class LabelView(GenericAPIView):

    queryset = Label.objects.all()
    serializer_class = CreateLabelSerializer

    def get(self, request, *args, **kwargs):

        try:
            labels = self.queryset
            return Response(labels.values(), status=status.HTTP_200_OK)
        except Exception:
            return Response(Exception, status=status.HTTP_403_FORBIDDEN)

    def post(self, request, *args, **kwargs):

        try:
            smd = {
                'Success': 'Fail',
                'message': 'Label creation Unsuccessful',
                'data': []
            }
            serializer = CreateLabelSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save(user_id=41)
                smd['Success'], smd['message'] = 'Success', 'Successfully created Label'
                return Response(smd, status=status.HTTP_201_CREATED)
            else:
                return Response(smd, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(Exception, status=status.HTTP_403_FORBIDDEN)


class LabelOperationsView(GenericAPIView):

    queryset = Label.objects.all()
    serializer_class = LabelOperationsSerializer

    def get(self, request, id, *args, **kwargs):

        try:
            smd = {
                'Success': 'Fail',
                'message': 'Unable to retrieve Label',
                'data': []
            }
            label = self.queryset.filter(pk=id)

            if label.values() is not None:
                smd['Success'], smd['message'], smd['data'] = 'Success', 'Successfully Retrieved Label', [label.values()]
                return Response(smd, status=status.HTTP_200_OK)
            else:
                return Response(smd, status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return Response(Exception, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, *args, **kwargs):

        try:
            smd = {
                'Success': 'Fail',
                'message': f'Unable to update Label with id : {id}',
                'data': []
            }

            serializer = LabelOperationsSerializer(data=request.data)

            if serializer.is_valid():

                label = self.queryset.get(pk=id)
                serializer.update(label, request.data)
                smd['message'], smd['message'] = 'Success', f'Successfully updated Label with id : {id}'
                return Response(smd, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return Response(Exception, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id, *args, **kwargs):

        try:
            smd = {
                'Success': 'Fail',
                'message': f'Unable to delete Label with id : {id}',
                'data': []
            }
            label = self.queryset.get(pk=id)

            if label is not None:
                label.delete()
                smd['Success'], smd['message'], smd['data'] = 'Success', f'Successfully deleted Label with id: {id}', \
                                                              [label.label_name]
                return Response(smd, status=status.HTTP_200_OK)
            else:
                return Response(smd, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(Exception, status=status.HTTP_404_NOT_FOUND)


class ViewArchivedNotes(GenericAPIView):

    def get(self, request, *args, **kwargs):

        try:
            archived_notes = Note.objects.all().filter(is_archived=True)
            return Response(archived_notes.values(), status=status.HTTP_200_OK)
        except Exception:
            return Response(Exception, status=status.HTTP_403_FORBIDDEN)


class ViewTrashedNotes(GenericAPIView):

    def get(self, request, *args, **kwargs):

        try:
            trashed_notes = Note.objects.all().filter(is_trashed=True)
            return Response(trashed_notes.values(), status=status.HTTP_200_OK)
        except Exception:
            return Response(Exception, status=status.HTTP_403_FORBIDDEN)
