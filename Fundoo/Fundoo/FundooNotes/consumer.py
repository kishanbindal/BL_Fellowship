from kafka import KafkaConsumer
from aiokafka import AIOKafkaConsumer
import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)


async def consume_data():
    loop = asyncio.get_event_loop()
    consumer = AIOKafkaConsumer('note_reminder', loop=loop, bootstrap_servers='localhost:9092')
    await consumer.start()
    try:
        async for message in consumer:
            logging.info('Got Message from Kafka')
            print(message)
    finally:
        await consumer.stop()

# def get_data_from_topic():
#
#     consumer = KafkaConsumer('note_reminder', bootstrap_servers='localhost:9092')
#     logging.info(f'{consumer.bootstrap_connected()}')


# def get_data_from_topic():
#
#     consumer = KafkaConsumer('note_reminder', bootstrap_servers='localhost:9092')
#     logging.info(f'{consumer.bootstrap_connected()}')

