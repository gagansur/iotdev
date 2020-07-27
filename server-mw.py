import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('192.168.1.190', 1026))
#serv.bind(('127.0.0.1', 1024))
serv.listen(5)
for i in range(1, 10):
    conn, addr = serv.accept()
    for j in range(1, 12000):
        data = conn.recv(4096)
        print (data)
        conn.send(b"I am SERVER")
conn.close()

