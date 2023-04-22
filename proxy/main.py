import os
import socket

UNICAST_PORT = 2001
MULTICAST_GROUP = os.getenv("MULTICAST_GROUP", "228.0.0.0")
MULTICAST_PORT = 2002
FORMATS = 7

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("proxy", 2000))

while True:
    request, address = sock.recvfrom(128)

    request = request.decode()

    if not request.startswith("get_result") or len(request.split()) != 2:
        sock.sendto(b'Wrong request!\n', address)
        continue

    format_name = request.split()[1]

    match format_name:
        case "pickle":
            sock.sendto(b'get_result\n', ("pickle", UNICAST_PORT))
        case "xml":
            sock.sendto(b'get_result\n', ("xml", UNICAST_PORT))
        case "json":
            sock.sendto(b'get_result\n', ("json", UNICAST_PORT))
        case "protobuf":
            sock.sendto(b'get_result\n', ("protobuf", UNICAST_PORT))
        case "avro":
            sock.sendto(b'get_result\n', ("avro", UNICAST_PORT))
        case "yaml":
            sock.sendto(b'get_result\n', ("yaml", UNICAST_PORT))
        case "message_pack":
            sock.sendto(b'get_result\n', ("message_pack", UNICAST_PORT))
        case "all":
            sock.sendto(b'get_result\n', (MULTICAST_GROUP, MULTICAST_PORT))
        case _:
            sock.sendto(b'Unknown format!\n', address)
            continue

    if format_name == "all":
        for _ in range(FORMATS):
            answer, _ = sock.recvfrom(128)
            sock.sendto(answer, address)
    else:
        answer, _ = sock.recvfrom(128)
        sock.sendto(answer, address)