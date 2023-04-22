import msgpack

from timeit import timeit

from lib.serve_answer import serve_answer

TEST_RUNS = 1000

class Structure:
    def __init__(self, dictionary, array):
        self.dictionary = dictionary
        self.array = array

data = Structure({str(i): i for i in range(10000)}, [i * 0.0001 for i in range(10000)])
serialized = msgpack.dumps(data.__dict__)

answer = "message_pack - "
answer += f"{len(serialized)} - "
answer += f"{timeit('msgpack.dumps(data.__dict__)', globals=globals(), number=TEST_RUNS) / TEST_RUNS * 1000:.2f}ms - "
answer += f"{timeit('msgpack.loads(serialized)', globals=globals(), number=TEST_RUNS) / TEST_RUNS * 1000:.2f}ms\n"

serve_answer("message_pack", answer)
