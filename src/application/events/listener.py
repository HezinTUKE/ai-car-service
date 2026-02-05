from aio_pika import connect_robust
from aio_pika.abc import AbstractMessage, AbstractChannel, AbstractRobustConnection

from application import config
from application.enums.rabbit_routers import RabbitRouter

mb_config = config.rabbitmq


class RabbitProcessorListener:
    def __init__(self, connection: AbstractRobustConnection, channel: AbstractChannel):
        self.connection = connection
        self.channel = channel

    @classmethod
    async def connect(cls):
        connection = await connect_robust(
            f"amqp://{mb_config.username}:{mb_config.password}@{mb_config.host}:{mb_config.port}/"
        )
        channel: AbstractChannel = await connection.channel()
        await channel.set_qos(prefetch_count=10)
        return cls(connection, channel)

    async def listen(self):
        exchange = await self.channel.declare_exchange(mb_config.exchange, "topic", durable=mb_config.durable)
        queue = await self.channel.declare_queue(mb_config.queue, durable=mb_config.durable)

        for router in RabbitRouter:
            await queue.bind(exchange, routing_key=f"*.{router.value}")

        await queue.consume(self.process_message)

    async def process_message(self, message: AbstractMessage):
        pass

    async def disconnect(self):
        await self.channel.close()
        await self.connection.close()
