from elasticsearch import Elasticsearch
import json
import logging
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from Fun.models import User
from util.decorators import logged_in
from.documents import NoteDocument
from .models import Note, Label
from .serializers import CreateNoteSerializer, NoteOperationsSerializer, CreateLabelSerializer, \
    LabelOperationsSerializer, SearchNoteSerializer
from Fundoo.redis_class import Redis
from services import TokenService
from .note_services import GenerateId
from rest_framework.views import APIView
rdb = Redis()
logging.basicConfig(level=logging.DEBUG)
es = Elasticsearch


@method_decorator(logged_in, name='dispatch')
class NoteView(GenericAPIView):

    # queryset = Note.objects.all()
    serializer_class = CreateNoteSerializer

    def get(self, request, *args, **kwargs):
        '''
        :param request:
        :return: Returns all Notes of specific user with Http 200. Exceptions return Http403. If token does not exist,
                returns Http 403
        '''
        try:
            import pdb
            # pdb.set_trace()

            user_id = GenerateId().generate_id(request)
            notes = Note.objects.filter(is_archived=False, is_trashed=False, user=user_id)
            serializer = CreateNoteSerializer(notes, many=True)
            logging.info(f'{serializer.data}')

            # notes = self.queryset.filter(is_archived=False, is_trashed=False, user_id=user_id)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        except Exception:
            return Response(Exception, status=status.HTTP_403_FORBIDDEN)

    def post(self, request, *args, **kwargs):
        '''
        :param request: HTTP Request containing Data being sent by the user
        :return: Http201 if Input is valid, else Http 400. If token not present/exceptions returns Http403
        '''

        smd = {
            'success': 'FAIL',
            'message': 'Failed To add Note to Server Database',
            'data': []
        }

        try:

            user_id = GenerateId().generate_id(request)
            # request.data['user'] = user_id
            serializer = CreateNoteSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save(user_id=user_id)
                data = serializer.data
                smd['success'], smd['message'] = 'Success', 'Note Successfully created'
                return JsonResponse(data=smd, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(Exception, status=status.HTTP_403_FORBIDDEN)


class NoteOperationsView(GenericAPIView):

    queryset = Note.objects.all()
    serializer_class = NoteOperationsSerializer

    @method_decorator(logged_in)
    def get(self, request, id, *args, **kwargs):
        '''
        :param request:
        :param id: Specified note ID
        :return: returns Note Value and Http 200 if found, else returns Http 400 if Note does not exist. Exceptions
                raise Http404
        '''
        try:

            smd = {
                'success': 'FAIL',
                'message': f'Unsuccessful in retrieving note with id : {id}',
                'data': []
            }
            user_id = GenerateId().generate_id(request)
            note = self.queryset.filter(pk=id, user_id=user_id)
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

    @method_decorator(logged_in)
    def put(self, request, id):
        '''
        :param request:
        :param id: Specified Note ID
        :return: returns Http200, if note is found and updated, else Http404. If input data is worng then, Http 400 is
                returned. Exceptions return Http 404.
        '''
        try:
            smd = {
                'Success': 'Fail',
                'message': 'Unsuccessful in updating Note',
                'data': [],
            }
            import json

            print(request.body)
            print('id::', id)
            # clientname = kwargs.get("clientname", "noparameter")
            # print("The searched name is: " + str(clientname))
            serializer = NoteOperationsSerializer(data=request.data) #json.loads(request.body)

            if serializer.is_valid():
                user_id = GenerateId().generate_id(request)
                note = Note.objects.get(pk=id)
                print(note, '---->')
                if note is not None:
                    serializer.update(note, serializer.data)
                    smd['Success'], smd['message'] = 'success', f'Successfully update Note with id: {id}'
                    return Response(smd, status=status.HTTP_200_OK)
                else:
                    return Response(smd, status=status.HTTP_404_NOT_FOUND)
            else:
                smd['data'] = [serializer.errors]
                return Response(smd, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(Exception, status=status.HTTP_404_NOT_FOUND)

    @method_decorator(logged_in)
    def delete(self, request, id):
        '''
        :param request:
        :param id: Specified Note ID
        :return: Deletes the specific Note with ID if note is found, else Http400. If no token, Http401 is returned
                from decorator
        '''
        smd = {
            'Success': 'Fail',
            'message': 'Deletion of Note Unsuccessful',
            'data': []
        }

        print(id)
        try:
            note = self.queryset.get(pk=id)
            if note is not None:
                print(note.delete())
                smd['Success'], smd['message'] = 'Success', 'Deletion of Note Successful'
                return Response(data=smd, status=status.HTTP_200_OK)
            else:
                return Response(smd, status=status.HTTP_400_BAD_REQUEST)
        except Note.DoesNotExist:
            return Response(smd, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response(Exception, status=status.HTTP_404_NOT_FOUND)


class LabelView(GenericAPIView):

    queryset = Label.objects.all()
    serializer_class = CreateLabelSerializer

    @method_decorator(logged_in)
    def get(self, request, *args, **kwargs):
        '''
        :param request:
        :return: Returns all labels of the specific user. if no token, Http403 is returned
        '''
        try:

            user_id = GenerateId().generate_id(request)
            labels = self.queryset.filter(user_id=user_id)
            return Response(labels.values(), status=status.HTTP_200_OK)
        except Exception:
            return Response(Exception, status=status.HTTP_403_FORBIDDEN)

    @method_decorator(logged_in)
    def post(self, request, *args, **kwargs):
        '''
        :param request: Takes in Label Details from request, with token
        :return: adds a label if successful else returns Http400. If token not present returns Http403
        '''
        try:
            smd = {
                'Success': 'Fail',
                'message': 'Label creation Unsuccessful',
                'data': []
            }
            serializer = CreateLabelSerializer(data=request.data)

            if serializer.is_valid():
                user_id = GenerateId().generate_id(request)
                serializer.save(user_id=user_id)
                smd['Success'], smd['message'] = 'Success', 'Successfully created Label'
                return Response(smd, status=status.HTTP_201_CREATED)
            else:
                return Response(smd, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(Exception, status=status.HTTP_403_FORBIDDEN)


class LabelOperationsView(GenericAPIView):

    queryset = Label.objects.all()
    serializer_class = LabelOperationsSerializer

    @method_decorator(logged_in)
    def get(self, request, id, *args, **kwargs):
        '''

        :param request:
        :param id: Label ID
        :return: returns the label with specified ID, if not found returns Http400. Exception Gives Http404
        '''
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

    @method_decorator(logged_in)
    def put(self, request, id, *args, **kwargs):
        '''
        :param request:
        :param id: Label ID
        :return: Updates the specified Label, returns Http200, if Input data mismatch then returns Http400, Http404 for
                    Exceptions
        '''
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

        except Label.DoesNotExist:
            return Response(smd, status=status.HTTP_404_NOT_FOUND)

        except Exception:
            return Response(Exception, status=status.HTTP_404_NOT_FOUND)

    @method_decorator(logged_in)
    def delete(self, request, id, *args, **kwargs):
        '''
        :param request:
        :param id: Note ID
        :return: Deletes Note with provided ID if label exists, else returns Http400, returns 404 for any Exception
        '''
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
        except Label.DoesNotExist:
            return Response(smd, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response(Exception, status=status.HTTP_404_NOT_FOUND)


class ViewArchivedNotes(GenericAPIView):

    @method_decorator(logged_in)
    def get(self, request, *args, **kwargs):
        '''
        :param request:
        :return: returns all archived notes by the user
        '''
        try:
            user_id = GenerateId().generate_id(request)
            archived_notes = Note.objects.all().filter(is_archived=True, user_id=user_id)
            return Response(archived_notes.values(), status=status.HTTP_200_OK)
        except Exception:
            return Response(Exception, status=status.HTTP_403_FORBIDDEN)


class ViewTrashedNotes(GenericAPIView):

    @method_decorator(logged_in)
    def get(self, request, *args, **kwargs):
        '''
        :param request:
        :return: Returns all Trashed Notes by the User
        '''
        try:
            user_id = GenerateId().generate_id(request)
            trashed_notes = Note.objects.all().filter(is_trashed=True, user_id=user_id)
            return Response(trashed_notes.values(), status=status.HTTP_200_OK)
        except Exception:
            return Response(Exception, status=status.HTTP_403_FORBIDDEN)


class ViewNotesReminder(GenericAPIView):

    @method_decorator(logged_in)
    def get(self, request, id=None):
        '''
        :param request: Request from User to see Notes with Reminders/Reminders
        :return: Returns all Notes with reminders pertaining to the User(Http200 Response).
                Any Exception raises an Http_400 Response from Server.
        '''
        try:

            user_id = GenerateId().generate_id(request)
            notes_with_reminder = Note.objects.filter(user_id=user_id, reminder__isnull=False)
            return Response(notes_with_reminder.values(), status=status.HTTP_200_OK)
        except Exception:
            smd = {'success': 'Fail', 'message': 'unable to retrieve notes with reminders', 'data': []}
            return Response(smd, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(logged_in, name='post')
class SearchNote(GenericAPIView):

    serializer_class = SearchNoteSerializer
    queryset = Note.objects.all()

    def post(self, request, id=None):
        '''
        :param request: Contains The fields that the User is going to be searching for
        :return: Returns Http200 if object is found/not found. if Not found, data is empty. Returns Http 400 if there
                is an issue with input.
        '''

        # search_parameters = request.data.get('title')
        serializer = SearchNoteSerializer(data=request.data)
        import pdb
        pdb.set_trace()

        if serializer.is_valid():

            user_id = GenerateId().generate_id(request)
            logging.info(f'----------->{user_id}')
            search_result = NoteDocument().search().query({
                'bool': {
                    'must': [
                        {'match': {'title': serializer.data.get('title')}},
                        {'match': {'note_text': serializer.data.get('note_text')}},
                        # {'match': {'labels': serializer.data.get('labels')}},
                        # {'match': {'color': serializer.data.get('color')}}
                        # 'type': "best_fields",
                        # 'field': ['title', 'note_text', 'reminder', 'color', 'labels']  #
                    ]
                    # 'tiebreaker': 0.5,
                }
            })
            result = search_result.execute()
            note_objs = [Note.objects.filter(user_id=user_id, title=hits.title, note_text=hits.note_text).values()
                         for hits in result.hits]
            logging.debug(f"{result}")
            # li = [hits.to_dict for hits in result.hits]
            smd = dict()
            smd['success'], smd['message'], smd['data'] = 'Success', 'Retrieved', note_objs
            return Response(smd, status=status.HTTP_200_OK)
        else:
            smd = dict()
            smd['success'], smd['message'] = 'Fail', 'Invalid Input/Serializer'
            return Response(data=smd, status=status.HTTP_400_BAD_REQUEST)
