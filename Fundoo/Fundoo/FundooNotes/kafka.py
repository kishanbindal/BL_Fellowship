from kafka import KafkaConsumer, KafkaProducer
import datetime
import logging
from rest_framework import status
from rest_framework.response import Response
from .models import Note
from Fun.models import User
from services import MailServices

logging.basicConfig(level=logging.DEBUG)


class KafkaMonitor:

    def __init__(self):
        self.host = 'localhost:9092'
        self.producer = self._create_producer()
        self.consumer = self._create_consumer()
        # self.topic = 'note_reminder'

    def _create_consumer(self):

        consumer = KafkaConsumer('note_reminder', bootstrap_servers=self.host)
        logging.info('Kafka Consumer Created')
        return consumer

    def _create_producer(self):

        producer = KafkaProducer(bootstrap_servers=[self.host])
        logging.info('Kafka Producer Created')
        return producer

    def send_data_to_kafka(self):

        notes_with_reminder = Note.objects.filter(reminder__isnull=True)
        for note in list(notes_with_reminder):
            print(note.reminder)
            self.producer.send('note_reminder', note.reminder, note.id)  # note.id
            self.producer.flush()
        # self.producer.send('note_reminder', notes_with_reminder)
        # self.producer.flush()
        logging.info('Message Posted To Kafka Topic')

    def consume_kafka_data(self):

        start = datetime.datetime.now()
        end = datetime.datetime.now() + datetime.timedelta(minutes=1)

        for note in self.consumer:
            print(note)
            self.consumer.close()

            # if start < note.reminder < end:
            #     user = User.objects.get(pk=note.user)
            #     MailServices().send_reminder(user, note)
            #     logging.info('Reminder Mail Sent')
            #     smd = {'success': 'Success', 'message': 'Mail Sent Successfully', 'data': []}
            #     # self.consumer.close()
            #     return Response(smd, status=status.HTTP_200_OK)
