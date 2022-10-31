import socket
import select
port = 60003
sockL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockL.bind(("", port))
sockL.listen(1)
listOfSockets = [sockL]
print("Listening on port {}".format(port))
def send_message(addr, message):
    for sockets in listOfSockets:
        if sockets != sockL:
            sockets.sendall(bytearray('Client: {} {}'.format(addr, message), 'ascii'))
while True:
    tup = select.select(listOfSockets, [], [])
    sock = tup[0][0]
    if sock == sockL:
        (sockClient, addr) = sockL.accept()
        listOfSockets.append(sockClient)
        send_message(addr, ' has connected\n')
    else:
        data = sock.recv(2048)
        if not data:
            send_message(str(sockClient.getpeername()), ' has disconnected\n')
            listOfSockets.remove(sockClient)
            sockClient.close()
        else:
            send_message(addr, data.decode('ascii'))