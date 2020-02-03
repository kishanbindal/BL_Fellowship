from kafka import KafkaProducer, SimpleProducer
from aiokafka import AIOKafkaProducer
import asyncio
import logging


logging.basicConfig(level=logging.DEBUG)


async def send_data_to_topic(data):

    loop = asyncio.get_event_loop()
    producer = AIOKafkaProducer(loop=loop, bootstrap_servers='localhost:9092')
    await producer.start()
    fut = await producer.send('note_reminder', data)
    msg = await fut

# def send_data_to_topic(data):
#     producer = SimpleProducer(bootstrap_server='localhost:9092', async=True)
#     producer.send_messages('note_reminder', data)
#     logging.info('Note Sent to Topic')

# def send_data_to_topic(data):
#     producer = KafkaProducer(bootstrap_server='localhost:9092')
#     producer.send('note_reminder', data)
#     logging.info('Note sent to Topic')
