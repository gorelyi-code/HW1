import fastavro

from io import BytesIO
from timeit import timeit

from lib.serve_answer import serve_answer

TEST_RUNS = 1000

schema = fastavro.parse_schema({
    "namespace": "structure",
    "type": "record",
    "name": "Structure",
    "fields": [
        {"name": "dictionary", "type": {"type": "map", "values": "int"}},
        {"name": "array", "type": {"type": "array", "items": "float"}}
    ]
})

data = {"dictionary": {str(i): i for i in range(10000)}, "array": [i * 0.0001 for i in range(10000)]}
buffer = BytesIO()
fastavro.schemaless_writer(buffer, schema, data)
buffer.seek(0)
serialized = buffer.read()

answer = "avro - "
answer += f"{len(serialized)} - "
answer += f"{timeit('fastavro.schemaless_writer(BytesIO(), schema, data)', globals=globals(), number=TEST_RUNS) / TEST_RUNS * 1000:.2f}ms - "
answer += f"{timeit('buffer.seek(0);fastavro.schemaless_reader(buffer, schema)', globals=globals(), number=TEST_RUNS) / TEST_RUNS * 1000:.2f}ms\n"

serve_answer("avro", answer)
