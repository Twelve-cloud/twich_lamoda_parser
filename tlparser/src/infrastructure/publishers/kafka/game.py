"""
game_publisher.py: File, containing kafka publisher class for twich game.
"""


from threading import Thread
from common.config import settings
from domain.events import TwichGameCreatedEvent, TwichGameDeletedEvent, TwichGameDomainEvent
from domain.interfaces.publishers import ITwichGamePublisher
from infrastructure.publishers.connections.kafka.producer import KafkaProducerConnection


class TwichGameKafkaPublisher(ITwichGamePublisher):
    """
    TwichGameKafkaPublisher: Kafka implementation publisher class for twich game.

    Args:
        IBasePublisher: Base publisher for TwichGameKafkaPublisher.
    """

    def __init__(self, kafka_producer: KafkaProducerConnection) -> None:
        """
        __init__: Initialize kafka twich game publisher.

        Args:
            kafka_producer (KafkaProducerConnection): Kafka producer connection.
        """

        self.producer = kafka_producer.producer

    async def publish(self, events: list[TwichGameDomainEvent]) -> None:
        """
        publish: Call handlers for every event.

        Args:
            events (list[E]): List of events.
        """

        for event in events:
            if isinstance(event, TwichGameCreatedEvent):
                await self.publish_game_created_event(event)
            elif isinstance(event, TwichGameDeletedEvent):
                await self.publish_game_deleted_event(event)

        return

    async def publish_game_created_event(self, event: TwichGameCreatedEvent) -> None:
        """
        publish_created_event: Publish game created event.

        Args:
            event (TwichGameCreatedEvent): Twich game created event.
        """

        Thread(
            target=self.producer.send,
            args=(settings.KAFKA_GAME_TOPIC, event),
            daemon=True,
        ).start()

    async def publish_game_deleted_event(self, event: TwichGameDeletedEvent) -> None:
        """
        publish_game_deleted_event: Publish game deleted event.

        Args:
            event (TwichGameDeletedEvent): Twich game deleted event.
        """

        Thread(
            target=self.producer.send,
            args=(settings.KAFKA_GAME_TOPIC, event),
            daemon=True,
        ).start()
