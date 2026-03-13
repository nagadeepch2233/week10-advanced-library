import time
import functools
from typing import Callable, Dict, Any

def retry_call(attempts: int = 3):

    def decorator(func: Callable):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            for i in range(1, attempts + 1):

                try:
                    return func(*args, **kwargs)

                except Exception as e:

                    print(f"[WARNING] Retry {i}/{attempts} failed:", e)

                    if i == attempts:
                        raise

                    time.sleep(1)

        return wrapper

    return decorator

def timed(func: Callable):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        print(f"[INFO] {func.__name__} executed in {end-start:.4f} seconds")

        return result

    return wrapper

class MemoryCache:

    def __init__(self, expire: int = 60):
        self.expire = expire
        self.cache: Dict[Any, tuple] = {}

    def __call__(self, func: Callable):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            key = (args, tuple(kwargs.items()))
            now = time.time()

            if key in self.cache:

                value, timestamp = self.cache[key]

                if now - timestamp < self.expire:
                    print("[DEBUG] Cache hit")
                    return value

            result = func(*args, **kwargs)

            self.cache[key] = (result, now)

            return result

        return wrapper
