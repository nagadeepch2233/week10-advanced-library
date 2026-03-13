from my_advanced_lib.core.generators import chunk_iterator

def test_chunk_iterator():

    data = range(10)

    batches = list(chunk_iterator(iter(data), size=3))

    assert len(batches) == 4
    assert batches[0] == [0, 1, 2]
    assert batches[-1] == [9]
