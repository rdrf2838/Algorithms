import socket

with socket.socket() as s:
    host=socket.gethostname()
    port=12345
    print(host)
    s.bind((host,port))
    s.listen(5)


    while True:
        c,addr=s.accept()
        print(b'got connection from'+str(addr).encode('utf-8'))
        c.send(b'thanks for connecting')
        c.close()