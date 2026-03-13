from my_advanced_lib.core.decorators import MemoryCache
from my_advanced_lib.core.generators import chunk_iterator

def test_cache_with_generator():

    cache = MemoryCache(expire=60)

    @cache
    def compute(x):
        return x * 2

    results = [compute(i) for i in range(5)]

    batches = list(chunk_iterator(iter(results), size=2))

    assert batches[0] == [0, 2]
    assert batches[1] == [4, 6]
