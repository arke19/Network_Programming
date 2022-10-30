import socket
import select
port = 60003
sockL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockL.bind(("", port))
sockL.listen(1)
listOfSockets = [sockL]
print("Listening on port {}".format(port))
while True:
    tup = select.select(listOfSockets, [], [])
    sock = tup[0][0]
    if sock == sockL:
        (sockClient, addr) = sockL.accept()
        listOfSockets.append(sockClient)
        for sockets in range(1,len(listOfSockets)):
                    listOfSockets[sockets].sendall(bytearray('Client: ' + str(sockClient.getpeername()) + ' has connected\n', 'ascii'))

    else:
        data = sock.recv(2048)
        if not data:
            for sockets in range(1,len(listOfSockets)):
                listOfSockets[sockets].sendall(bytearray('Client: ' + str(sockClient.getpeername()) + ' has disconnected\n', 'ascii'))
            listOfSockets.remove(sockClient)
            sockClient.close()
        else:
            for sockets in range(1,len(listOfSockets)):
                    listOfSockets[sockets].sendall(bytearray(str(sockClient.getpeername()) + ': ' + data.decode('ascii'), 'ascii'))

