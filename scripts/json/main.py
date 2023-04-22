import json

from timeit import timeit

from lib.serve_answer import serve_answer

TEST_RUNS = 1000

class Structure:
    def __init__(self, dictionary, array):
        self.dictionary = dictionary
        self.array = array

data = Structure({str(i): i for i in range(10000)}, [i * 0.0001 for i in range(10000)])
serialized = json.dumps(data.__dict__)

answer = "json - "
answer += f"{len(serialized)} - "
answer += f"{timeit('json.dumps(data.__dict__)', globals=globals(), number=TEST_RUNS) / TEST_RUNS * 1000:.2f}ms - "
answer += f"{timeit('json.loads(serialized)', globals=globals(), number=TEST_RUNS) / TEST_RUNS * 1000:.2f}ms\n"

serve_answer("json", answer)
