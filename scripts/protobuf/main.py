import structure_pb2

from timeit import timeit

from lib.serve_answer import serve_answer

TEST_RUNS = 1000

data = structure_pb2.Structure()
for i in range(10000):
    data.dictionary[str(i)] = i 
data.array.extend([i * 0.0001 for i in range(10000)])
serialized = data.SerializeToString()

answer = "protobuf - "
answer += f"{len(serialized)} - "
answer += f"{timeit('data.SerializeToString()', globals=globals(), number=TEST_RUNS) / TEST_RUNS * 1000:.2f}ms - "
answer += f"{timeit('data.FromString(serialized)', globals=globals(), number=TEST_RUNS) / TEST_RUNS * 1000:.2f}ms\n"

serve_answer("protobuf", answer)
