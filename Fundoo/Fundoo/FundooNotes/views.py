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
from services import TokenService, CollaboratorService
from .note_services import GenerateId

rdb = Redis()
logging.basicConfig(level=logging.DEBUG)


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

            user_id = GenerateId().generate_id(request)
            notes = Note.objects.filter(is_archived=False, is_trashed=False, user=user_id)
            # print(notes,'---->notes')
            # obj=notes.first()
            # print(obj.note_image.url,'------>url')
            collaborated_notes = Note.objects.filter(is_archived=False, is_trashed=False).filter(collaborators=user_id)
            user_notes_serializer = CreateNoteSerializer(notes, many=True)
            collab_notes_serializer = CreateNoteSerializer(collaborated_notes, many=True)
            if len(list(notes)) > 0:
                for data in user_notes_serializer.data:
                    name_list = []
                    for collaborator in data['collaborators']:
                        user = User.objects.get(pk=3)
                        # if user.email not in name_list:
                        name_list.append(user.pk)
                    data['collaborators'] = name_list

            if len(list(collaborated_notes)) > 0:
                for data in collab_notes_serializer.data:
                    name_list = []
                    for collaborator in data['collaborators']:
                        user = User.objects.get(pk=collaborator)
                        # if user.email not in name_list:
                        name_list.append(user.pk)
                    data['collaborators'] = name_list
                # collab_notes_serializer.data['collaborators'] = name_list
            output_data = user_notes_serializer.data + collab_notes_serializer.data
            # logging.info(f'{output_data}')

            smd = {'success': True, 'message': 'Successfully collected all notes', 'data': output_data}

            # notes = self.queryset.filter(is_archived=False, is_trashed=False, user_id=user_id)
            return Response(data=smd, status=status.HTTP_200_OK)

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
            #

            user_id = GenerateId().generate_id(request)
            # request.data['user'] = user_id

            import pdb
            pdb.set_trace()

            if 'note_image' in request.data:

                other_data = json.loads(request.data.get('otherData'))
                img_file = request.data.get('note_image')
                data = other_data
                data['note_image'] = img_file
                serializer = CreateNoteSerializer(data=data)

                # to_merge = json.loads(request.data.get('otherData'))
                # request.data.update(to_merge)
                # serializer = CreateNoteSerializer(data=request.data)
            else:
                data = request.data.dict()['otherData']
                data = json.loads(data)
                serializer = CreateNoteSerializer(data=data, partial=True)

            # collab = request.data.get('collaborators')
            # collab_list = []
            #
            # if len(collab)>0:
            #     for username in collab:
            #         user = User.objects.get(username=username)
            #         collab_list.append(user.id)
            #     request.data['collaborators'] = collab_list

            print(request.data, '------->re')

            # serializer = CreateNoteSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save(user_id=user_id)
                logging.info(f'POST METHOD SERIALIZER DATA  {serializer.data}')
                smd['success'], smd['message'] = True, 'Note Successfully created'
                print(serializer.data,'---->ser')

                return Response(data=smd, status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors, '---->error')

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
    def patch(self, request, id):
        '''
        :param request:
        :param id: Specified Note ID
        :return: returns Http200, if note is found and updated, else Http404. If input data is worng then, Http 400 is
                returned. Exceptions return Http 404.
        '''
        try:
            smd = {
                'success': False,
                'message': 'Unsuccessful in updating Note',
                'data': [],
            }

            import json

            # collab = request.data.get('collaborators')
            # collab_list = []

            # if collab is not None:
            #     for email in collab:
            #         user = User.objects.get(email=email)
            #         collab_list.append(user.id)
            # request.data['collaborators'] = collab_list

            serializer = NoteOperationsSerializer(data=request.data, partial=True) #json.loads(request.body)

            # import pdb
            # pdb.set_trace()

            if serializer.is_valid():
                # serializer.data['collaborators'] = CollaboratorService().get_collaborators(serializer)
                user_id = GenerateId().generate_id(request)
                id = request.data.get('id')
                note = Note.objects.get(pk=id)
                # logging.info(f'PUT METHOD DATA : {serializer.data}')
                if note is not None:
                    serializer.update(note, serializer.validated_data)
                    smd['success'], smd['message'] = True, f'Successfully update Note with id: {id}'
                    return Response(data=smd, status=status.HTTP_200_OK)
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
            smd = {
                'success': True,
                'message': 'Successfully retrieved labels',
                'data': labels.values()
            }
            return Response(data=smd, status=status.HTTP_200_OK)
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
                'success': 'Fail',
                'message': 'Label creation Unsuccessful',
                'data': []
            }

            serializer = CreateLabelSerializer(data=request.data)

            if serializer.is_valid():
                user_id = GenerateId().generate_id(request)
                serializer.save(user_id=user_id)
                smd['success'], smd['message'] = True, 'Successfully created Label'
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
                'Success': False,
                'message': 'Unable to retrieve Label',
                'data': []
            }
            label = self.queryset.filter(pk=id)

            if label.values() is not None:
                smd['Success'], smd['message'], smd['data'] = True, 'Successfully Retrieved Label', [label.values()]
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

            import pdb
            pdb.set_trace()

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
                'success': False,
                'message': f'Unable to delete Label with id : {id}',
                'data': []
            }
            label = self.queryset.get(pk=id)

            if label is not None:
                label.delete()
                smd['success'], smd['message'], smd['data'] = True, f'Successfully deleted Label with id: {id}', \
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

        smd = {
            'success': False,
            'message': 'Unsuccessful in retrieving archived notes',
            'data': []
        }

        try:
            user_id = GenerateId().generate_id(request)
            archived_notes = Note.objects.all().filter(is_archived=True, user_id=user_id)
            serializer = CreateNoteSerializer(archived_notes, many=True)  # TODO
            smd['success'], smd['message'], smd['data'] = True, 'Retrieved Archived Notes', serializer.data
            return Response(data=smd, status=status.HTTP_200_OK)
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
            serializer = CreateNoteSerializer(trashed_notes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
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
            serializer = CreateNoteSerializer(notes_with_reminder, many=True)
            smd = {'success': True, 'message': 'Successfully Retrieved notes with reminders',
                   'data': serializer.data}
            return Response(data=smd, status=status.HTTP_200_OK)
        except Exception:
            smd = {'success': False, 'message': 'unable to retrieve notes with reminders', 'data': []}
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
        serializer = SearchNoteSerializer(data=request.data, partial=True)

        if serializer.is_valid():

            user_id = GenerateId().generate_id(request)
            logging.info(f'----------->{user_id}')
            search_result = NoteDocument().search().query({
                'bool': {
                    'must': [
                        {'match': {'title': serializer.data.get('title')}},
                        {'match': {'note_text': serializer.data.get('title')}},
                        # {'match': {'labels': serializer.data.get('labels')}},
                        # {'match': {'color': serializer.data.get('color')}}
                        # 'type': "best_fields",
                        # 'field': ['title', 'note_text', 'reminder', 'color', 'labels']  #
                    ]
                    # 'tiebreaker': 0.5,
                },
                # 'nested':
            })
            # import pdb
            # pdb.set_trace()
            result = search_result.execute()
            note_objs = [Note.objects.filter(user_id=user_id, title=hits.title, note_text=hits.note_text).values()
                         for hits in result.hits]
            # TODO
            output_data = []
            for query_obj in note_objs:
                output_data.append(query_obj[0])
            logging.debug(f"{output_data}")
            # li = [hits.to_dict for hits in result.hits]
            smd = dict()
            smd['success'], smd['message'], smd['data'] = True, 'Retrieved', output_data
            return Response(smd, status=status.HTTP_200_OK)
        else:
            smd = dict()
            smd['success'], smd['message'] = False, 'Invalid Input/Serializer'
            return Response(data=smd, status=status.HTTP_400_BAD_REQUEST)
