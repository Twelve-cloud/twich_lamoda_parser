"""
stream_repository.py: File, containing repository abstract class for a twich stream.
"""


from abc import abstractmethod
from domain.entities.twich.stream_entity import TwichStreamEntity
from domain.events.twich.stream_events import (
    PublicParseStreamCalledEvent,
    TwichStreamCreatedOrUpdatedEvent,
    TwichStreamDeletedByUserLoginEvent,
)
from domain.interfaces.repositories.base.base_repository import IBaseRepository


class ITwichStreamRepository(IBaseRepository[TwichStreamEntity, TwichStreamCreatedOrUpdatedEvent]):
    """
    ITwichStreamRepository: Abstract class for twich stream repositories.

    Args:
        IBaseRepository (TwichStreamEntity): IBaseRepository for ITwichStreamRepository.
    """

    @abstractmethod
    async def parse_stream(self, user_login: str) -> PublicParseStreamCalledEvent:
        """
        parse_stream: Return event about parsing twich stream.

        Args:
            user_login (str): Login of the user.

        Returns:
            PublicParseStreamCalledEvent: Event about parsing twich stream.
        """

        pass

    @abstractmethod
    async def delete_stream_by_user_login(
        self,
        user_login: str,
    ) -> TwichStreamDeletedByUserLoginEvent:
        """
        delete_stream_by_user_login: Delete stream by user login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichStreamDeletedByUserLoginEvent: Event about deleting twich stream.
        """

        pass

    @abstractmethod
    async def get_stream_by_user_login(self, user_login: str) -> TwichStreamEntity:
        """
        get_stream_by_user_login: Return stream by user login.

        Args:
            user_login (str): Login of the user.

        Returns:
            TwichStreamEntity: Twich stream entity.
        """

        pass
