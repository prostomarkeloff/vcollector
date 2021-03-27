from vcollector.collector import AbstractCollector
from aiofile import AIOFile
from vcollector.collector import AnyEvent
from vcollector.formatter import format

class FileCollector(AbstractCollector):
    def __init__(self, file_name: str):
        self.fn = file_name

    async def is_suitable(self, event: AnyEvent) -> bool:
        return True

    async def collect(self, event: AnyEvent):
        async with AIOFile(self.fn, "a") as f:
            await f.write(format(event) + "\n")


