import time
from my_advanced_lib.core.decorators import MemoryCache

def slow_function(x):

    time.sleep(0.01)

    return x * x

cache = MemoryCache(expire=60)

@cache
def cached_function(x):

    time.sleep(0.01)

    return x * x

print("Performance Comparison")
print("-" * 30)

start = time.perf_counter()

for i in range(20):
    slow_function(10)

end = time.perf_counter()

print("Without Cache:", end - start, "seconds")

start = time.perf_counter()

for i in range(20):
    cached_function(10)

end = time.perf_counter()

print("With Cache:", end - start, "seconds")
