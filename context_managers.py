from contextlib import contextmanager
import time

@contextmanager
def timer_context(name: str):

    start = time.time()

    yield

    end = time.time()

    print(f"{name} finished in {end-start:.4f} seconds")
