import typing

from vcollector.collector import AbstractCollector

AIOFile: typing.Union[None, typing.Callable]
try:
    from aiofile import AIOFile
except ImportError:
    AIOFile = None
from vcollector.collector import AnyEvent
from vcollector.formatter import AbstractFormatter


class FileCollector(AbstractCollector):
    def __init__(self, fmt: AbstractFormatter, file_name: str):
        self.fn = file_name
        self._fmt = fmt

    def formatter(self) -> AbstractFormatter:
        return self._fmt

    async def is_suitable(self, event: AnyEvent) -> bool:
        return True

    async def collect(self, event: AnyEvent):
        if AIOFile:
            async with AIOFile(self.fn, "a") as f:  # type: ignore
                await f.write(await self.formatter().fmt(event) + "\n")
        else:
            with open(self.fn, "a") as f:
                f.write(await self.formatter().fmt(event) + "\n")
