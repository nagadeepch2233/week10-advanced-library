import pytest
from my_advanced_lib.core.decorators import retry_call, timed, MemoryCache

def test_retry_success():

    @retry_call(attempts=2)
    def success():
        return 100

    assert success() == 100

def test_retry_failure():

    @retry_call(attempts=2)
    def fail():
        raise ValueError("error")

    with pytest.raises(ValueError):
        fail()

def test_cache_hit():

    cache = MemoryCache(expire=60)

    calls = {"count": 0}

    @cache
    def add(x):
        calls["count"] += 1
        return x + 1

    assert add(5) == 6
    assert add(5) == 6

    # Should only execute once
    assert calls["count"] == 1

def test_timer_decorator():

    @timed
    def square(x):
        return x * x

    assert square(4) == 16
