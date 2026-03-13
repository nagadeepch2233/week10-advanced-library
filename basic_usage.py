from my_advanced_lib.core.decorators import retry_call, timed, MemoryCache
from my_advanced_lib.core.generators import chunk_iterator
import random

print("Basic Usage Example")
print("-" * 30)

cache = MemoryCache(expire=60)

@retry_call(attempts=3)
@timed
@cache
def fetch_user_data(endpoint: str):

    if random.random() < 0.3:
        raise ConnectionError("API temporarily unavailable")

    return {"user": "Alice", "endpoint": endpoint}

data = fetch_user_data("https://api.example.com/user")

print("Result:", data)

print("\nCalling again (should use cache):")

data2 = fetch_user_data("https://api.example.com/user")

print("Cached Result:", data2)

print("\nGenerator Example")

dataset = range(10)

for batch in chunk_iterator(iter(dataset), size=3):
    print("Batch:", batch)
