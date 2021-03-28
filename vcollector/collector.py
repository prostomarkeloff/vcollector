from abc import ABC, abstractmethod
from vkwave.bots.core.dispatching.events.base import BotEvent, UserEvent

from vcollector.formatter import AbstractFormatter
from logging import getLogger
from typing import Union, List

logger = getLogger(__name__)

AnyEvent = Union[BotEvent, UserEvent, Union[BotEvent, UserEvent]]


class AbstractCollector(ABC):
    @abstractmethod
    def formatter(self) -> AbstractFormatter:
        ...

    @abstractmethod
    async def is_suitable(self, event: AnyEvent) -> bool:
        ...

    @abstractmethod
    async def collect(self, event: AnyEvent):
        ...


class CollectorManager:
    def __init__(self, collectors: List[AbstractCollector]):
        self.collectors = collectors

    def add_collector(self, collector: AbstractCollector):
        self.collectors.append(collector)

    async def collect(self, event: AnyEvent):
        for collector in self.collectors:
            if await collector.is_suitable(event):
                await collector.collect(event)
