import socket

host = 'localhost'
port = 80

server_socket = socket.socket(
        family=socket.AF_INET, type=socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen(1)
print('Listening on port %s ...' % port)

while True:
    connection, address = server_socket.accept()

    request = connection.recv(1024).decode()
    print(request)
    
    #send http
    response = ('HTTP/1.0 200 OK\n\nYour Browser sent the following request\n\n' + str(request))
    connection.sendall(response.encode())
    connection.close()

server_socket.close()
