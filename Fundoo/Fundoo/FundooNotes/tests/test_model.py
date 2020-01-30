import pytest
from Fun.models import User
from FundooNotes.models import Note


@pytest.mark.django_db
class TestNoteModel:

    @pytest.fixture()
    def set_up(self):

        email = 'kishan.bindal@gmail.com'
        password = '123'

        user1 = User.objects.create_user(username='kishanbindal', email=email, password=password, is_active=True)
        user1.save()

        user2 = User.objects.create_user(username='kb', email='kb@gmail.com', password=123, is_active=True)
        user2.save()
        note1 = Note(user_id=user1.id, title="Shopping List", note_text="Vegetables", note_image='',
                     is_archived=False, is_trashed=False, color='', is_pinned=False, link='', reminder=None)
        note1.save()

        note2 = Note(user_id=user2.id, title="Destination List", note_text="List of destinations", note_image=None,
                     is_archived=False, is_trashed=False, color='', is_pinned=False, link='', reminder=None)
        note2.save()

        return note1, note2

    def test_str_dunder(self, set_up):
        note1, note2 = set_up
        assert(note1.__str__(), note1.title)
        assert(note2.__str__(), note2.title)

    def test_model_fields(self, set_up):
        note1, note2 = set_up
        assert(note1.title, 'Shopping List')
        assert(note1.note_text, "Vegetables")
        assert(note1.is_archived, False)
