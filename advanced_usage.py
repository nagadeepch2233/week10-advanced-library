from my_advanced_lib.core.generators import chunk_iterator

print("Advanced Usage Example")
print("-" * 30)

def process_data(data):
    return data * 2

def filter_even(data):
    return data % 2 == 0

dataset = range(20)

processed = map(process_data, dataset)

filtered = filter(filter_even, processed)

for batch in chunk_iterator(filtered, size=4):
    print("Processed Batch:", batch)
