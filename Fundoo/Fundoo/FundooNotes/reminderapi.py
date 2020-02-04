from .kafka import KafkaMonitor
import logging

logging.basicConfig(level=logging.DEBUG)


def start_kafka():
    return KafkaMonitor()


def check_for_reminders():
    kafka = start_kafka()
    kafka.send_data_to_kafka()
    kafka.consume_kafka_data()
    logging.info('Data Retrieved From Kafka')
