from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from .models import Note

# connections.create_connection(hosts=['localhost:9200'], timeout=20)

note = Index('note')
note.settings(
    number_of_shards=1,
    number_of_replicas=0
)

custom_analyzer = analyzer("custom_analyzer",
                           tokenizer="standard",
                           char_filter=["html_strip"],
                           filter=["ngram", "stop", "snowball"])


@registry.register_document
class NoteDocument(Document):

    labels = fields.ObjectField(properties={
        "label_name": fields.TextField(analyzer=custom_analyzer),
        "user": fields.TextField(analyzer=custom_analyzer)
    })

    #collB

    class Django:

        model = Note
        fields = [
            'title',
            'note_text',
            'reminder',
            'color',
        ]

    class Index:

        name = 'note'

# class NoteDocument(Document):
#
#     title = field.Text(analyzer=custom_analyzer)
#     # note_text = field.Text(analyzer=custom_analyzer)
#     # reminder = field.Date(default_timezone='UTC')
#     # color = field.Text(analyzer=custom_analyzer)
#     # labels = field.Object(properties={"label_name": field.Text(analyzer=custom_analyzer),
#     #                                   "user": field.Text(analyzer=custom_analyzer)})
#
#     class Index:
#
#         # name of the Elastic Search Index
#         name = 'note'
#         settings = {
#             'number_of_shards': 1,
#             'number_of_replicas': 0
#         }
#
#     class Django:
#         model = Note
#
#
# NoteDocument.init()
