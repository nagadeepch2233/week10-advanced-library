from my_advanced_lib.core.context_managers import timer_context

def test_timer_context():

    with timer_context("test-block"):
        x = sum(range(1000))

    assert x > 0
