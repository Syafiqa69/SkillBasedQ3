import socket

def main():
    # Get user input for pressure value in bar
    pressure_bar = float(input("Enter pressure value in bar: "))

    # Create client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_address = ('192.168.248.134', 8484)  # Server IP address
    client_socket.connect(server_address)

    # Send pressure value to the server (as a string)
    client_socket.send(str(pressure_bar).encode())

    # Receive the converted pressure from the server
    pressure_atm = client_socket.recv(1024).decode()

    # Display the received atmosphere-standard value
    print(f"Atmosphere-Standard value received from the server: {pressure_atm} atm")

    # Close the connection with the server
    client_socket.close()

if __name__ == "__main__":
    main()
