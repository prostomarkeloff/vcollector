from abc import ABC, abstractmethod
from vkwave.bots.core.dispatching.events.base import BotEvent, BaseEvent, UserEvent
from vkwave.bots.core.types.bot_type import BotType

from vcollector.formatter import format
from logging import getLogger
from typing import Union, List

logger = getLogger(__name__)

AnyEvent = Union[BotEvent, UserEvent, Union[BotEvent, UserEvent]]

class AbstractCollector(ABC):
    @abstractmethod
    async def is_suitable(self, event: AnyEvent) -> bool:
        ...

    @abstractmethod
    async def collect(self, event: AnyEvent):
        ...


class LoggingCollector(AbstractCollector):
    async def is_suitable(self, event: AnyEvent) -> bool:
        return True
        
    async def collect(self, event: AnyEvent):
        formatted = format(event)

        logger.info(f"New message!\n{formatted}")


class CollectorManager:
    def __init__(self, collectors: List[AbstractCollector]):
        self.collectors = collectors

    def add_collector(self, collector: AbstractCollector):
        self.collectors.append(collector)

    async def collect(self, event: AnyEvent):
        for collector in self.collectors:
            if await collector.is_suitable(event):
                await collector.collect(event)
