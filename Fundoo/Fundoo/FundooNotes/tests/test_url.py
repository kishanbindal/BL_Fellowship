from django.urls import reverse, resolve


class TestFundooUrls:

    def test_notes(self):

        path = reverse('notes')
        assert resolve(path).view_name == 'notes'

    def test_notes_with_id(self):
        path = reverse('notes-op', kwargs={"id": 1})
        assert resolve(path).view_name == 'notes-op'

    def test_labels(self):

        path = reverse('labels')
        assert resolve(path).view_name == 'labels'

    def test_labels_with_id(self):

        path = reverse('labels-op', kwargs={"id": 5})
        assert resolve(path).view_name == 'labels-op'

    def test_archived(self):

        path = reverse('archived-notes')
        assert resolve(path).view_name == 'archived-notes'

    def test_trashed(self):

        path = reverse('trashed-notes')
        assert resolve(path).view_name == 'trashed-notes'

    def test_reminders(self):

        path = reverse('reminder')
        assert resolve(path).view_name == 'reminder'
