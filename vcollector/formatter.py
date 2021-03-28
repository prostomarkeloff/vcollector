from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vcollector.collector import AnyEvent

from vkwave.bots.core.types.bot_type import BotType


class AbstractFormatter(ABC):
    @abstractmethod
    async def fmt(self, event: "AnyEvent") -> str:
        ...


class DefaultFormatter(AbstractFormatter):
    async def fmt(self, event: "AnyEvent") -> str:
        result: str
        if event.bot_type is BotType.BOT:
            m = event.object.object.message
            result = f"text: {m.text}; from_id: {m.from_id}; peer_id: {m.peer_id}"
        else:
            raise NotImplementedError()
        return result
