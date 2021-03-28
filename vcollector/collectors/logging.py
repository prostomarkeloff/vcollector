from vcollector.collector import AbstractCollector, AnyEvent
from vcollector.formatter import AbstractFormatter
import logging


class LoggingCollector(AbstractCollector):
    def __init__(self, fmt: AbstractFormatter, logger: logging.Logger):
        self._fmt = fmt
        self._logger = logger

    def formatter(self) -> AbstractFormatter:
        return self._fmt

    async def is_suitable(self, event: AnyEvent) -> bool:
        return True

    async def collect(self, event: AnyEvent):
        formatted = await self.formatter().fmt(event)

        self._logger.info(f"New message!\n{formatted}")
