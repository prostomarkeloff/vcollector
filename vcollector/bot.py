from vkwave.bots.easy.easy_bot import SimpleLongPollBot
from vkwave.bots.core.dispatching.events.base import BotEvent
from logging import basicConfig, getLogger

from vcollector.collector import CollectorManager, LoggingCollector
from vcollector.collectors import FileCollector

TOKEN = ""
GROUP_ID = 

bot = SimpleLongPollBot(TOKEN, GROUP_ID)
mn = bot.event_type_filter("message_new")

logger = getLogger(__name__)
basicConfig(level="INFO")

manager = CollectorManager([LoggingCollector(), FileCollector("log.txt")])

@bot.message_handler()
async def handler(event: bot.SimpleBotEvent) -> None:
    await manager.collect(event)
    return

def run():
    logger.info("Starting bot...")
    bot.run_forever()
