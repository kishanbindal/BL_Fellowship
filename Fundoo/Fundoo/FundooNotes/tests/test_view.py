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
import mock


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

        return response.data.get('token')

    def test_get_note_by_id(self, set_up):

        path = reverse('notes-op', kwargs={"id": 8})
        request = RequestFactory().get(path)
        headers = {'token': set_up}
        request.headers = headers
        response = FundooNotes.views.NoteOperationsView.get(self, request)
        assert response.status_code == 200

    def test_get_note_by_id_without_token(self):

        path = reverse('notes-op', kwargs={"id": 8})
        request = RequestFactory().get(path)
        response = FundooNotes.views.NoteOperationsView.get(self, request)
        assert response.status_code == 401

    # def test_update_note(self, set_up):
    #
    #     path = reverse('notes-op', kwargs={"id": 3})
    #     request = RequestFactory().put(path)
    #     headers = {'token': set_up}
    #     request.headers = headers
    #     data = {"title": "Title of My note", "note_text": 'Note Sent', "note_image": None, "labels": [],
    #             "collaborators": [],
    #             "is_archived": "True", "is_trashed": "False", "color": "", "is_pinned": "False", "link": "",
    #             "reminder": None,
    #             }
    #     request.data = data
    #     response = FundooNotes.views.NoteOperationsView.put(self, request)
    #     assert response.status_code == 200

    # def test_delete_note(self, set_up):
    #
    #     path = reverse('notes-op', kwargs={"id": 8})
    #     headers = set_up
    #     request = RequestFactory().delete(path)
    #     request.headers = {
    #         'token': headers
    #     }
    #     response = FundooNotes.views.NoteOperationsView.delete(self, request)
    #     assert response.status_code == 200
# TODO Delete, Put

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
        return response.data.get('token')

    def test_get_label_by_id(self, set_up):

        headers = {
            'token': set_up
        }
        path = reverse('labels-op', kwargs={"id": 8})
        request = RequestFactory().get(path)
        request.headers = headers
        response = FundooNotes.views.LabelOperationsView.get(self, request)
        assert response.status_code == 200

    def test_get_label_by_id_no_token(self):

        path = reverse('labels-op', kwargs={"id": 8})
        request = RequestFactory().get(path)
        response = FundooNotes.views.LabelOperationsView.get(self, request)
        assert response.status_code == 401
# TODO Delete, PUT


@pytest.mark.django_db
class TestArchivedNotes:

    @pytest.fixture
    def set_up(self):
        
        user = User.objects.create_user(username='kb', email='kb@gmail.com', password=123, is_active=True)
        user.save()
        path = reverse('login')
        request = RequestFactory().post(path)
        request.data = {
            'email': user.email,
            'password': user.password
        }
        response = views.UserLoginView.post(self, request)
        token = response.data.get('token')

        note1 = FundooNotes.models.Note(user_id=user.id, title="Shopping List", note_text="Vegetables", note_image='',
                     is_archived=False, is_trashed=False, color='', is_pinned=False, link='', reminder=None)
        note1.save()

        note2 = FundooNotes.models.Note(user_id=user.id, title="Destination List", note_text="List of destinations", note_image=None,
                     is_archived=True, is_trashed=False, color='', is_pinned=False, link='', reminder=None)
        note2.save()

        return note1, note2, token

    def test_view_archived_notes(self, set_up):
        note1, note2, token = set_up
        path = reverse('archived-notes')
        headers = {
            'token': token
        }
        request = RequestFactory().get(path)
        request.headers = headers
        response = FundooNotes.views.ViewArchivedNotes.get(self, request)
        assert response.status_code == 200

    def test_view_archived_notes_no_token(self, set_up):
        note1, note2, token = set_up
        path = reverse('archived-notes')
        request = RequestFactory().get(path)
        response = FundooNotes.views.ViewArchivedNotes.get(self, request)
        assert response.status_code == 401
