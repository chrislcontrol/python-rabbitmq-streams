import asyncio
import sys

from rstream import Producer

STREAM_NAME = "first-stream"
STREAM_RETENTION = 5000000000  # 5GB


async def publish_msg(msg):
    async with Producer(host="localhost", username="guest", password="guest", port=5552) as producer:
        await producer.create_stream(STREAM_NAME, exists_ok=True, arguments={"MaxLengthBytes": STREAM_RETENTION})
        await producer.send(stream=STREAM_NAME, message=msg.encode('utf-8'))

        print('Message has been published.')


if __name__ == '__main__':
    asyncio.run(publish_msg(sys.argv[0]))
