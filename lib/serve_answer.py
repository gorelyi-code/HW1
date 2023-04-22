import os
import select
import socket
import struct

UNICAST_PORT = 2001
MULTICAST_GROUP = os.getenv("MULTICAST_GROUP", "228.0.0.0")
MULTICAST_PORT = 2002

def serve_answer(format_name, answer):
    socket_unicast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_multicast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    socket_unicast.bind((format_name, UNICAST_PORT))
    socket_multicast.bind((MULTICAST_GROUP, MULTICAST_PORT))

    mreq = struct.pack("=4sl", socket.inet_aton(MULTICAST_GROUP), socket.INADDR_ANY)
    socket_multicast.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    sockets = [socket_unicast, socket_multicast]

    while True:
        ready_sockets, _, _ = select.select(sockets, [], [])

        for sock in ready_sockets:
            sock.recvfrom(128)

            sock.sendto(answer.encode(), ("proxy", 2000))
