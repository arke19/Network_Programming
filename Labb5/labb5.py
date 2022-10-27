import socket

host = '127.0.0.1'
port = 60003

server_score = 0
client_score = 0

moves = ['R', 'P', 'S']


def server():

    outcome = [' You lost! current score is:',
               ' You won! current score is:',
               ' Its a draw! current score is:']

    server_socket = socket.socket(
        family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)

    welcome_message = "Welcome to rock, paper, sciccors start by inputing R,P or S. First to 10 points win"

    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    conn.sendall(bytearray(welcome_message, 'ascii'))

    while True:
        data = conn.recv(1024)
        if not data:
            break
        client_message = str(data.decode('ASCII'))
        if client_message in moves:
            server_answer = input(
                ('({},{}) Your move: '.format(server_score, client_score)))
            server_move = server_answer[-1]
            if server_move == client_message:
                print(outcome[3])
                conn.send(outcome[3].encode)
            elif server_move == "R" and client_message == "P" or server_move == "S" and client_message == "R":
                client_score += 1
                print(outcome[1])
                conn.send(outcome[2].encode)
            else:
                server_score += 1
                print(outcome[2])
                conn.send(outcome[1].encode)
        #conn.send(data.encode())


def client():
    client_socket = socket.socket(
        family=socket.AF_INET, type=socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        #client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print('Server sent: ' + data)
        message = input(
            ('({},{}) Your move: '.format(server_score, client_score)))
        client_move = message[-1]
        while client_move not in moves:
            print("wrong input!")
            print(client_move)
            client_move = input(
                ('({},{}) Your move: '.format(server_score, client_score)))
        else:
          client_socket.send(client_move.encode())


if __name__ == "__main__":
    print("Select if you're a server (s) or client (c)")
    user_input = input()
    if user_input == "s":
        server()
    elif user_input == "c":
        client()
    else:
        print("wrong input enter 'server' or 'client'")
