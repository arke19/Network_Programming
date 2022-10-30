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
        pass
    # TODO: A new clients connects.
    # call (sockClient, addr) = sockL.accept() and take care of the new client
    # add the new socket to listOfSockets
    # notify all other clients about the new client
    else:
        # Connected clients send data or are disconnecting...
        data = sock.recv(2048)
    if not data:
      pass
    # TODO: A client disconnects
    # close the socket object and remove from listOfSockets
    # notify all other clients about the disconnected client
    else:
        pass
    # TODO: A client sends a message
    # data is a message from a client
    # send the data to all clients
