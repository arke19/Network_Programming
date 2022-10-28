import socket

host = '127.0.0.1'
port = 60003

player_one = 0
player_two = 0

moves = ['R', 'P', 'S']

def checkWinner(server_move, client_move):
    global player_one
    global player_two
    if server_move == client_move:
        pass
    elif server_move == "R" and client_move == "P" or server_move == "S" and client_move == "R":
        player_two += 1
    elif server_move == "P" and client_move == "R" or server_move == "R" and client_move == "S":
        player_one += 1



def play_round(socket_connection):
    while True:
        if player_one == 10:
            print((' You won with: {} to {}'.format(player_one, player_two)))
            break
        elif player_two == 10:
            print((' You lost with: {} to {}'.format(player_one, player_two)))
            break
        input_move = input(
                ('({},{}) Your move: '.format(player_one, player_two)))
        your_move = input_move[-1]
            
        while your_move not in moves:
            print("wrong input. R, S or P are valid inputs")
            input_move = input(
                ('({},{}) Your move: '.format(player_one, player_two)))
            your_move = input_move[-1]

        socket_connection.sendall(bytearray(your_move, 'ascii'))
        data = socket_connection.recv(1024)
        opponent_move = str(data.decode('ASCII'))

        checkWinner(your_move, opponent_move)



def server():
    server_socket = socket.socket(
        family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)


    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    play_round(conn)


def client():
    client_socket = socket.socket(
        family=socket.AF_INET, type=socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    play_round(client_socket)


if __name__ == "__main__":
    print("Select if you're a server (s) or client (c)")
    user_input = input()
    if user_input == "s":
        server()
    elif user_input == "c":
        client()
    else:
        print("wrong input enter 's' or 'c'")
