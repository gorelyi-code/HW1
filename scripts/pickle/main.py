import pickle

from timeit import timeit

from lib.serve_answer import serve_answer

TEST_RUNS = 1000

class Structure:
    def __init__(self, dictionary, array):
        self.dictionary = dictionary
        self.array = array

data = Structure({str(i): i for i in range(10000)}, [i * 0.0001 for i in range(10000)])
serialized = pickle.dumps(data)

answer = "pickle - "
answer += f"{len(serialized)} - "
answer += f"{timeit('pickle.dumps(data)', globals=globals(), number=TEST_RUNS) / TEST_RUNS * 1000:.2f}ms - "
answer += f"{timeit('pickle.loads(serialized)', globals=globals(), number=TEST_RUNS) / TEST_RUNS * 1000:.2f}ms\n"

serve_answer("pickle", answer)
