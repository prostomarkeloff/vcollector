import typing
import logging

from vkwave.bots import MiddlewareResult, BaseMiddleware, BaseEvent, BotType, BotEvent
from vcollector.collector import CollectorManager


class VCollectorMiddleware(BaseMiddleware):
    def __init__(self, manager: CollectorManager):
        self._mn = manager

    async def pre_process_event(self, event: BaseEvent) -> MiddlewareResult:
        if event.bot_type is BotType.BOT and event.object.type == "message_new":
            logging.debug("Got bot event and it's 'message_new', logging it.")
            await self._mn.collect(typing.cast(BotEvent, event))
            return MiddlewareResult(True)
        elif event.bot_type is BotType.BOT:
            logging.debug("Got bot event but it's not 'message_new', skipping it")
            return MiddlewareResult(True)
        else:
            logging.debug("Got user event, skipping it")
            return MiddlewareResult(True)
