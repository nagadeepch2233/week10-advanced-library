from typing import Iterator

def chunk_iterator(data: Iterator, size: int = 1000):

    batch = []

    for item in data:

        batch.append(item)

        if len(batch) == size:
            yield batch
            batch = []

    if batch:
        yield batch
