# Intro

It was some project what about I have forgotten. So, I publishing it only because it's related to vkwave. Enjoy.

# What?
VCollector is a middleware for vkwave, written for logging purposes.

Example

```python
from vkwave.bots import SimpleLongPollBot
from logging import basicConfig, getLogger

from vcollector.collector import CollectorManager
from vcollector.formatter import DefaultFormatter
from vcollector.collectors import FileCollector, LoggingCollector
from vcollector.middleware import VCollectorMiddleware

TOKEN, GROUP_ID = "", 123

bot = SimpleLongPollBot(TOKEN, GROUP_ID)

logger = getLogger(__name__)
basicConfig(level="DEBUG")

fmt = DefaultFormatter()
manager = CollectorManager(
    [LoggingCollector(fmt, getLogger("bot_logging")), FileCollector(fmt, "log.txt")]
)

bot.add_middleware(VCollectorMiddleware(manager))


@bot.message_handler()
async def handler(event: bot.SimpleBotEvent) -> str:
    return "hi bud"


def run():
    logger.info("Starting bot...")
    bot.run_forever()


run()
```


