import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("UTF-8")}')
        sock.send(b'ACK')

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    # backlog connection
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        # client connects, `client` client socket, `address` connection details
        # passed to thread object.
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        # thread object pointing to `handle_client()`
        client_handler = threading.Thread(target=handle_client, args=(client,))
        # start thread to handle connection
        client_handler.start()

if __name__ == '__main__':
    main()