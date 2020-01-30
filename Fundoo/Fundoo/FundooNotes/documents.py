from elasticsearch_dsl import analyzer, connections, Document, field, Keyword, tokenizer
from .models import Note

connections.create_connection(alias='searchnote', hosts=['localhost'], timeout=20)

custom_analyzer = analyzer("custom_analyzer",
                           tokenizer="standard",
                           char_filter=["html_strip"],
                           filter=["lowercase", "stop", "snowball", "whitespace"])


class NoteDocument(Document):

    title = field.Text(analyzer=custom_analyzer)
    note_text = field.Text(analyzer=custom_analyzer)
    reminder = field.Date(default_timezone='UTC')
    color = field.Text(analyzer=custom_analyzer)
    labels = field.Object(properties={"label_name": field.Text(analyzer=custom_analyzer),
                                      "user": field.Text(analyzer=custom_analyzer)})

    class Index:

        # name of the Elastic Search Index
        name = 'Note'
        settings = {
            'number_of_shard': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Note


NoteDocument.init()
