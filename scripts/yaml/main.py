import yaml
from yaml.loader import BaseLoader

from timeit import timeit

from lib.serve_answer import serve_answer

TEST_RUNS = 1000

class Structure:
    def __init__(self, dictionary, array):
        self.dictionary = dictionary
        self.array = array

data = Structure({str(i): i for i in range(100)}, [i * 0.0001 for i in range(100)])
serialized = yaml.dump(data)

answer = "yaml - "
answer += f"{len(serialized)} - "
answer += f"{timeit('yaml.dump(data)', globals=globals(), number=TEST_RUNS) / TEST_RUNS * 1000:.2f}ms - "
answer += f"{timeit('yaml.load(serialized, Loader=BaseLoader)', globals=globals(), number=TEST_RUNS) / TEST_RUNS * 1000:.2f}ms\n"

serve_answer("yaml", answer)
