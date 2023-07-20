import socket

def convert_to_atmosphere(pressure_bar):
    # Convert pressure from bar to atmosphere (1 bar = 0.986923 atm)
    return pressure_bar * 0.986923

def handle_client(client_socket):
    try:
        # Receive data from the client (assuming pressure value is sent as a string)
        data = client_socket.recv(1024).decode()
        pressure_bar = float(data)

        # Convert pressure to atmosphere-standard
        pressure_atm = convert_to_atmosphere(pressure_bar)

        # Send the converted pressure back to the client
        client_socket.send(str(pressure_atm).encode())
    except Exception as e:
        print('Error occurred during communication:', str(e))

    # Close the connection with the client
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the server socket to a specific address and port
    server_address = ('192.168.248.134', 8484)
    server_socket.bind(server_address)

    # Listen for incoming connections (max 5 connections in the queue)
    server_socket.listen(5)

    print('Server is listening on {}:{}'.format(*server_address))

    while True:
        print('Waiting for a client to connect...')
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print('Client connected:', client_address)

        # Handle the client request in a separate function
        handle_client(client_socket)

if __name__ == '__main__':
    main()
