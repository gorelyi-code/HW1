from dict2xml import dict2xml
import xmltodict

from timeit import timeit

from lib.serve_answer import serve_answer

TEST_RUNS = 1000

class Structure:
    def __init__(self, dictionary, array):
        self.dictionary = dictionary
        self.array = array

data = Structure({str(i): i for i in range(100)}, [i * 0.0001 for i in range(100)])
serialized = dict2xml(data.__dict__, wrap ='root')

answer = "xml - "
answer += f"{len(serialized)} - "
answer += f"""{timeit('dict2xml(data.__dict__, wrap = "root")', globals=globals(), number=TEST_RUNS) / TEST_RUNS * 1000:.2f}ms - """
answer += f"{timeit('xmltodict.parse(serialized)', globals=globals(), number=TEST_RUNS) / TEST_RUNS * 1000:.2f}ms\n"

serve_answer("xml", answer)
