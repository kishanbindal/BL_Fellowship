from kafka import KafkaConsumer, KafkaProducer
import datetime
import logging
import pytz
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

        consumer = KafkaConsumer('note_reminder', bootstrap_servers=self.host,
                                 consumer_timeout_ms=500,
                                 group_id=None, auto_offset_reset='earliest')  # value_deserializer=lambda x: x.decode('utf-8'),
        logging.info('Kafka Consumer Created')
        return consumer

    def _create_producer(self):

        producer = KafkaProducer(bootstrap_servers=[self.host])
        logging.info('Kafka Producer Created')
        return producer

    def send_data_to_kafka(self):

        notes_with_reminder = list(Note.objects.filter(reminder__isnull=False))
        timezone = pytz.timezone("UTC")
        if len(notes_with_reminder) > 0:
            for note in list(notes_with_reminder):
                t = type(note.reminder)
                logging.info(f'TYPE OF REMINDER -------------->>>> {t}')
                if t is None or note.reminder == '':
                    break
                reminder_time = note.reminder
                reminder_time_byte = str.encode(str(reminder_time))
                note_id = str.encode(str(note.id))
                self.producer.send('note_reminder', reminder_time_byte, note_id)  # (topic, value, key)
                self.producer.flush()
        logging.info('Message Posted To Kafka Topic')

    def consume_kafka_data(self):

        today = str(datetime.datetime.now().date())

        for note in self.consumer:
            logging.info(f'{note.topic}---------{note.value}--------{note.key}')
            reminder_time = note.value.decode('utf-8')
            list_reminder_time = reminder_time.split()
            note_id = note.key.decode('utf-8')
            if list_reminder_time[0] == today:
                note_being_analysed = Note.objects.get(pk=77)
                user = User.objects.get(pk=note_being_analysed.user_id)
                MailServices().send_reminder(user, note_being_analysed)
                logging.info('Reminder Mail Sent')
                smd = {'success': 'Success', 'message': 'Mail Sent Successfully', 'data': []}
                # self.consumer.close()
                return Response(smd, status=status.HTTP_200_OK)
        self.consumer.close()
