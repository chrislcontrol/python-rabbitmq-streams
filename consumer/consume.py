import asyncio

from rstream import (
    AMQPMessage,
    Consumer,
    MessageContext,
    ConsumerOffsetSpecification,
    OffsetType
)


async def run_consumer():
    consumer = Consumer(host="localhost", username="guest", password="guest", port=5552)
    await consumer.start()
    print('Consuming...')

    await consumer.subscribe(
        stream="first-stream",
        callback=on_message,
        offset_specification=ConsumerOffsetSpecification(OffsetType.FIRST, None)
    )

    await consumer.run()

    return consumer


async def on_message(msg: AMQPMessage | bytes, message_context: MessageContext):
    stream = message_context.consumer.get_stream(message_context.subscriber_name)
    print("Got message: {} from stream {}".format(msg.decode('utf-8'), stream))


if __name__ == '__main__':
    asyncio.run(run_consumer())
