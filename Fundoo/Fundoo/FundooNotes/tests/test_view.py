from django.test import Client, RequestFactory
from django.urls import reverse
import pytest
import requests
from unittest.mock import patch
from services import TokenService
from util.decorators import logged_in
from Fun.models import User
from Fun import views
import FundooNotes
from FundooNotes.models import Note, Label
import mock

BASE_URL = 'http://127.0.0.1:8000/'


@pytest.mark.django_db
class TestNoteView:

    @pytest.fixture()
    def set_up(self):

        email = 'kishan.bindal@gmail.com'
        password = '123'

        user = User.objects.create_user(username='kishanbindal', email=email, password=password, is_active=True)
        user.save()
        path = reverse('login')
        request = RequestFactory().post(path)
        request.data = {
            'email': email,
            'password': password
        }
        response = views.UserLoginView.post(self, request)
        return response.data.get('token')

    def test_note_view_get(self, set_up):

        headers = set_up
        headers = {
            'Content-Type': 'application/json',
            'token': headers
        }
        response = requests.get(url='http://127.0.0.1:8000/notes/api/notes/', headers=headers)
        # print(r,'--->r')
        # request = RequestFactory().get(path)
        # request.headers = headers
        # response = client.get(path, headers=headers)
        # response = FundooNotes.views.NoteView.get(self, request)
        assert response.status_code == 200

    def test_note_view_without_token(self, set_up):

        headers = {
            'Content-Type': 'application/json',
            'token': None,
        }
        response = requests.get(url='http://127.0.0.1:8000/notes/api/notes/', headers=headers)
        assert response.status_code == 401

    def test_note_view_wrong_token(self):

        headers = {
            'token': 'byJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImFiYyJ9.zIVQLO-ZB6lVQXph3faTxfovtIAByaH8v1c2ZRMpVbI'
        }
        path = reverse('notes')
        request = RequestFactory().get(path)
        request.headers = headers
        response = FundooNotes.views.NoteView.get(self, request)
        assert response.status_code == 403

    def test_note_view(self, set_up):

        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(url='http://127.0.0.1:8000/notes/api/notes/', headers=headers)
        assert response.status_code == 401

    def test_note_post(self, set_up):

        path = reverse('notes')
        headers = set_up
        headers = {
            'token': headers
        }
        data = {"title": "Title of My note", "note_text": 'Note Sent', "note_image": None, "labels": [],
                "collaborators": [],
                "is_archived": "False", "is_trashed": "False", "color": "", "is_pinned": "False", "link": "",
                "reminder": None,
                }
        request = RequestFactory().post(path)
        request.data = data
        request.headers = headers
        response = FundooNotes.views.NoteView.post(self, request)
        notes = FundooNotes.models.Note.objects.all()
        print(notes)
        assert response.status_code == 201

    def test_note_post_without_token(self):

        path = reverse('notes')
        data = {"title": "Title of My note", "note_text": 'Note Sent', "note_image": None, "labels": [],
                "collaborators": [],
                "is_archived": "False", "is_trashed": "False", "color": "", "is_pinned": "False", "link": "",
                "reminder": None,
                }
        request = RequestFactory().post(path)
        request.data = data
        response = FundooNotes.views.NoteView.post(self, request)
        assert response.status_code == 403

    def test_note_post_invalid_serializer(self, set_up):

        path = reverse('notes')
        data = {"title": "Title of My note", "note_text": None, "note_image": None, "labels": [],
                "collaborators": [], "is_archived": "False", "is_trashed": "False", "color": "", "is_pinned": "False",
                "link": "", "reminder": None
                }
        headers = {
            'token': set_up
        }
        request = RequestFactory().post(path)
        request.data = data
        request.headers = headers
        response = FundooNotes.views.NoteView.post(self, request)
        assert response.status_code == 400


@pytest.mark.django_db
class TestNoteOperationsView:

    queryset = FundooNotes.models.Note.objects.all()

    @pytest.fixture
    def set_up(self):

        email = 'kishan.bindal@gmail.com'
        password = '123'

        user = User.objects.create_user(username='kishanbindal', email=email, password=password, is_active=True)
        user.save()
        path = reverse('login')
        request = RequestFactory().post(path)
        request.data = {
            'email': email,
            'password': password
        }
        response = views.UserLoginView.post(self, request)
        note = Note(user_id=user.id, title="Title of My note", note_text='Note Sent', note_image=None, is_archived=True,
                    is_trashed=False, color="", is_pinned=False, link="", reminder=None,)
        note.save()
        print(note.pk, '===========NOTE ID============')
        return response.data.get('token'), note.pk

    def test_get_note_by_id(self, set_up):

        path = reverse('notes-op', kwargs={"id": 8})
        request = RequestFactory().get(path)
        headers = {'token': set_up[0]}
        request.headers = headers
        response = FundooNotes.views.NoteOperationsView.get(self, request)
        assert response.status_code == 200

    def test_get_note_by_id_without_token(self):

        path = reverse('notes-op', kwargs={"id": 8})
        request = RequestFactory().get(path)
        response = FundooNotes.views.NoteOperationsView.get(self, request)
        assert response.status_code == 401

    def test_get_note_by_id_wrong_token(self):

        path = reverse('notes-op', kwargs={"id": 8})
        headers = {
            'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjR9.bQzPrAnhZwvT1e5X3ILJU1WgvOs0dEsAVuna6mtwKHg'
        }
        request = RequestFactory().get(path)
        request.headers = headers
        response = FundooNotes.views.NoteOperationsView.get(self, request)
        assert response.status_code == 400

    def test_update_note(self, set_up):

        token, note_id = set_up
        path = reverse('notes-op', args=[note_id])
        print(f'Path =======> {path}')
        headers = {'HTTP_TOKEN': token}
        data = {
            "title": "Changed title of my Note", "note_text": "Not Updated!!!", "note_image": None,
            "is_archived": False, "is_trashed": False, "color": "", "labels": [], "is_pinned": False, "link": "",
            'collaborators': [], "reminder": None
            }
        client = Client()
        response = client.put(path, data=data, content_type='application/json', **headers)
        assert response.status_code == 200

    def test_update_note_no_token(self, set_up):

        token, note_id = set_up
        path = reverse('notes-op', args=[note_id])
        print(f'Path =======> {path}')
        headers = {'HTTP_TOKEN': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImFiY2QxMDAifQ.NkSXJBoHozYOHfJwxw9FWS4Cz-nRjHP1FtXd2UlmMx0'}
        data = {
            "title": "Changed title of my Note", "note_text": "Not Updated!!!", "note_image": None,
            "is_archived": False, "is_trashed": False, "color": "", "labels": [], "is_pinned": False, "link": "",
            'collaborators': [], "reminder": None
        }
        client = Client()
        response = client.put(path, data=data, content_type='application/json', **headers)
        assert response.status_code == 400

    def test_delete_note(self, set_up):

        token, note_id = set_up
        path = reverse('notes-op', args=[note_id])
        print(path)
        client = Client()
        headers = {'HTTP_TOKEN': token}
        response = client.delete(path=path, content_type='application/json', **headers)
        assert response.status_code == 200

    def test_delete_note_wrong_token(self, set_up):

        token, note_id = set_up
        path = reverse('notes-op', args=[note_id])
        client = Client()
        headers = {'HTTP_TOKEN': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImFiY2QxMDAifQ.NkSXJBoHozYOHfJwxw9FWS4Cz-nRjHP1FtXd2UlmMx0'}
        response = client.delete(path, content_type='application/json', **headers)
        assert response.status_code == 400

    def test_delete_note_no_token(self, set_up):

        note_id = set_up[1]
        path = reverse('notes-op', args=[note_id])
        client = Client()
        response = client.delete(path, content_type='application/json')
        assert response.status_code == 401

    def test_delete_note_wrong_note_id(self, set_up):

        token = set_up[0]
        path = reverse('notes-op', args=[100])
        headers = {'HTTP_TOKEN': token}
        client = Client()
        response = client.delete(path, content_type='application/json', **headers)
        assert response.status_code == 404


@pytest.mark.django_db
class TestLabelView:

    queryset = FundooNotes.models.Label.objects.all()

    @pytest.fixture
    def set_up(self):

        email = 'kishan.bindal@gmail.com'
        password = '123'

        user = User.objects.create_user(username='kishanbindal', email=email, password=password, is_active=True)
        user.save()
        path = reverse('login')
        request = RequestFactory().post(path)
        request.data = {
            'email': email,
            'password': password
        }
        response = views.UserLoginView.post(self, request)
        return response.data.get('token')

    def test_get_label_all(self, set_up):

        headers = {
            "token": set_up
        }

        path = reverse('labels')
        request = RequestFactory().get(path)
        request.headers = headers
        response = FundooNotes.views.LabelView.get(self, request)
        assert response.status_code == 200

    def test_get_label_all_no_token(self, set_up):

        path = reverse('labels')
        request = RequestFactory().get(path)
        response = FundooNotes.views.LabelView.get(self, request)
        assert response.status_code == 401

    def test_post_label(self, set_up):

        headers = {
            'token': set_up
        }
        path = reverse('labels')
        request = RequestFactory().post(path)
        request.data = {
            'label_name': "New Label"
        }
        request.headers = headers
        response = FundooNotes.views.LabelView.post(self, request)
        assert response.status_code == 201

    def test_post_label_no_token(self, set_up):

        path = reverse('labels')
        request = RequestFactory().post(path)
        request.data = {
            'label_name': "New Label"
        }
        response = FundooNotes.views.LabelView.post(self, request)
        assert response.status_code == 401

    def test_post_label_no_data(self, set_up):

        headers = {
            'token': set_up
        }
        path = reverse('labels')
        request = RequestFactory().post(path)
        request.headers = headers
        response = FundooNotes.views.LabelView.post(self, request)
        assert response.status_code == 403

    def test_post_label_invalid_serializer(self, set_up):

        headers = {
            'token': set_up
        }
        path = reverse('labels')
        request = RequestFactory().post(path)
        request.data = {
            'label_name': None
        }
        request.headers = headers
        response = FundooNotes.views.LabelView.post(self, request)
        assert response.status_code == 400


@pytest.mark.django_db
class TestLabelOperationsView:

    queryset = FundooNotes.models.Label.objects.all()

    @pytest.fixture
    def set_up(self):

        email = 'kishan.bindal@gmail.com'
        password = '123'

        user = User.objects.create_user(username='kishanbindal', email=email, password=password, is_active=True)
        user.save()
        path = reverse('login')
        request = RequestFactory().post(path)
        request.data = {
            'email': email,
            'password': password
        }
        response = views.UserLoginView.post(self, request)
        label = Label(label_name='NEW TEST LABEL', user_id=user.id)
        label.save()
        return response.data.get('token'), label.id

    def test_get_label_by_id(self, set_up):

        token, label_id = set_up
        headers = {
            'token': token
        }
        path = reverse('labels-op', args=[label_id])
        request = RequestFactory().get(path)
        request.headers = headers
        response = FundooNotes.views.LabelOperationsView.get(self, request)
        assert response.status_code == 200

    def test_get_label_by_id_no_token(self, set_up):

        label_id = set_up[1]
        path = reverse('labels-op', args=[label_id])
        request = RequestFactory().get(path)
        response = FundooNotes.views.LabelOperationsView.get(self, request)
        assert response.status_code == 401

    def test_get_label_wrong_token(self, set_up):

        label_id = set_up[1]
        path = reverse('labels-op', args=[label_id])
        headers = {'HTTP_TOKEN': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjAxNTQ2NDI1In0.UTMDxj2pEoHVGaGtfO0eLovJHW5IeXnXMytGxmsOwy4'}
        client = Client()
        response = client.get(path, content_type='application/json', **headers)
        assert response.status_code == 400

    def test_update_label_by_id(self, set_up):

        token, label_id = set_up
        path = reverse('labels-op', args=[label_id])
        headers = {'HTTP_TOKEN': token}
        data = {
            'label_name': 'LABEL NAME HAS BEEN UPDATED'
        }
        client = Client()
        response = client.get(path, data=data, content_type='application/json', **headers)
        assert response.status_code == 200

    def test_update_label_no_token(self, set_up):

        label_id = set_up[1]
        path = reverse('labels-op', args=[label_id])
        data = {'label_name': "LABEL NAME IS BEING UPDATED"}
        client = Client()
        response = client.put(path, data=data, content_type='application/json')
        assert response.status_code == 401

    def test_update_label_wrong_token(self, set_up):

        label_id = set_up[1]
        path = reverse('labels-op', args=[label_id])
        data = {'label_name': 'Attempting to change label name'}
        headers = {'HTTP_TOKEN': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjAxNTQ2NDI1In0.UTMDxj2pEoHVGaGtfO0eLovJHW5IeXnXMytGxmsOwy4'}
        client = Client()
        response = client.put(path, data=data, content_type='application/json', **headers)
        assert response.status_code == 400

    # def test_update_label_does_not_exist(self, set_up):
    #
    #     token = set_up[0]
    #     path = reverse('labels-op', args=[15])
    #     headers = {'HTTP_TOKEN': token}
    #     data = {'label_name': 'Changing Label Name'}
    #     client = Client()
    #     response = client.put(path, data=data, content_type='application/json', **headers)
    #     assert response.status_code == 404

    def test_delete_label(self, set_up):

        token, label_id = set_up
        headers = {'HTTP_TOKEN': token}
        path = reverse('labels-op', args=[label_id])
        client = Client()
        response = client.delete(path, content_type='application/json', **headers)
        assert response.status_code == 200

    def test_delete_label_no_token(self, set_up):

        label_id = set_up[1]
        path = reverse('labels-op', args=[label_id])
        client = Client()
        response = client.delete(path, content_type='application/json')
        assert response.status_code == 401

    def test_delete_label_invalid_label(self, set_up):

        token = set_up[0]
        headers = {'HTTP_TOKEN': token}
        path = reverse('labels-op', args=[100])
        client = Client()
        response = client.delete(path, content_type='application/type', **headers)
        assert response.status_code == 404

    def test_delete_label_invalid_token(self, set_up):

        label_id = set_up[1]
        headers = {'HTTP_TOKEN': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImFiY2QxMDAifQ.NkSXJBoHozYOHfJwxw9FWS4Cz-nRjHP1FtXd2UlmMx0'}
        path = reverse('labels-op', args=[label_id])
        client = Client()
        response = client.delete(path, content_type='application/json', **headers)
        assert response.status_code == 400


@pytest.mark.django_db
class TestArchivedNotes:

    @pytest.fixture
    def set_up(self):

        email = 'kishan.bindal@gmail.com'
        password = '123'

        user = User.objects.create_user(username='kishanbindal', email=email, password=password, is_active=True)
        user.save()
        path = reverse('login')
        request = RequestFactory().post(path)
        request.data = {
            'email': email,
            'password': password
        }
        response = views.UserLoginView.post(self, request)
        return response.data.get('token')

    def test_view_archived_notes(self, set_up):

        token = set_up
        path = reverse('archived-notes')
        headers = {
            'token': token
        }
        request = RequestFactory().get(path)
        request.headers = headers
        response = FundooNotes.views.ViewArchivedNotes.get(self, request)
        assert response.status_code == 200

    def test_view_archived_notes_no_token(self):

        path = reverse('archived-notes')
        request = RequestFactory().get(path)
        response = FundooNotes.views.ViewArchivedNotes.get(self, request)
        assert response.status_code == 401

    def test_view_archived_notes_invalid_token(self):

        path = reverse('archived-notes')
        headers = {
            'token': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImFiYyJ9.zIVQLO-ZB6lVQXph3faTxfovtIAByaH8v1c2ZRMpVbI"
        }
        request = RequestFactory().get(path)
        request.headers = headers
        response = FundooNotes.views.ViewArchivedNotes.get(self, request)
        assert response.status_code == 400


@pytest.mark.django_db
class TestViewTrashedNotes:

    @pytest.fixture
    def set_up(self):

        email = 'kishan.bindal@gmail.com'
        password = '123'

        user = User.objects.create_user(username='kishanbindal', email=email, password=password, is_active=True)
        user.save()
        path = reverse('login')
        request = RequestFactory().post(path)
        request.data = {
            'email': email,
            'password': password
        }
        response = views.UserLoginView.post(self, request)
        return response.data.get('token')

    def test_view_trashed_notes(self, set_up):

        headers = {
            'token': set_up
        }
        path = reverse('trashed-notes')
        request = RequestFactory().get(path)
        request.headers = headers
        response = FundooNotes.views.ViewTrashedNotes.get(self, request)
        assert response.status_code == 200

    def test_view_trashed_notes_without_token(self):

        path = reverse('trashed-notes')
        request = RequestFactory().get(path)
        response = FundooNotes.views.ViewTrashedNotes.get(self, request)
        assert response.status_code == 401

    def test_view_trashed_notes_wrong_token(self):

        path = reverse('trashed-notes')
        headers = {
            'token': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImFiYyJ9.zIVQLO-ZB6lVQXph3faTxfovtIAByaH8v1c2ZRMpVbI"
        }
        request = RequestFactory().get(path)
        request.headers = headers
        response = FundooNotes.views.ViewTrashedNotes.get(self, request)
        assert response.status_code == 400


# @pytest.mark.django_db
# class TestViewReminderNotes:
#
#     @pytest.fixture
#     def set_up(self):
#
#         email = 'kishan.bindal@gmail.com'
#         password = '123'
#
#         user = User.objects.create_user(username='kishanbindal', email=email, password=password, is_active=True)
#         user.save()
#         path = reverse('login')
#         request = RequestFactory().post(path)
#         request.data = {
#             'email': email,
#             'password': password
#         }
#         response = views.UserLoginView.post(self, request)
#         token = response.data.get('token')
#
#         note = Note(user_id=user.id, title="Note Title", note_text='Note Content', note_image=None, is_archived=True,
#                     is_trashed=False, color="", is_pinned=False, link="", reminder='2020-02-05 12:34:33+00:00')
#
#         # note = Note(user_id=user.id, title="Title of My note", note_text='Note Sent', note_image=None, is_archived=True,
#         #             is_trashed=False, color="", is_pinned=False, link="", reminder='2020-02-05 12:34:33+00:00')
#         # note.collaborators.set([])
#         # note.labels.set([])
#         note.save()
#         return token
#
#     def test_view_reminder_success(self, set_up):
#
#         path = reverse('reminder')
#         headers = {'HTTP_TOKEN': set_up}
#         client = Client()
#         response = client.get(path, content_type='application/json', **headers)
#         assert response.status_code == 200
#
#     def test_view_reminder_wrong_token(self, set_up):
#
#         path = reverse('reminder')
#         headers = {'HTTP_TOKEN': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImFiYyJ9.zIVQLO-ZB6lVQXph3faTxfovtIAByaH8v1c2ZRMpVbI"}
#         client = Client()
#         response = client.get(path, content_type='application/json', **headers)
#         assert response.status_code == 400
#
#     def test_view_reminder_no_token(self, set_up):
#
#         path = reverse('reminder')
#         client = Client()
#         response = client.get(path, content_type='application/json')
#         assert response.status_code == 401
#
#
# @pytest.mark.django_db
# class TestElasticSearch:
#
#     @pytest.fixture
#     def set_up(self):
#
#         user = User(username='kishan', email='kishan@gmail.com', password='123', is_active=True)
#         user.save()
#         path = reverse('login')
#         request = RequestFactory().get(path)
#         request.data = {'email': 'kishan@gmail.com', 'password': '123'}
#         response = views.UserLoginView.post(self, request)
#         token = response.data.get('token')
#         return token
#
#     def test_search_view_success(self, set_up):
#
#         path = reverse('search')
#         request = RequestFactory().get(path)
#         request.headers = {'token': set_up}
#         request.data = {
#             'title': 'Note Title',
#             'note_text': 'Note Content',
#             'color': '#e8eb34',
#             'reminder': 'null',
#             # 'labels': '',
#         }
#         response = FundooNotes.views.SearchNote.get(self, request)
#         assert response.status_code == 200
