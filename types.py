from typing import Callable, Iterator, Any

Processor = Callable[[dict], dict]
DataStream = Iterator[Any]
