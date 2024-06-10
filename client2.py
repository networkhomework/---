import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 6666        # The port used by the server

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            username = input("Enter your username: ")
            operation = input("Enter operation (balance, deposit, withdraw): ").lower()
            if operation == 'deposit' or operation == 'withdraw':
                amount = int(input("Enter amount: "))
            else:
                amount = 0

            request = f"{username}|{operation}|{amount}"
            s.sendall(request.encode())

            data = s.recv(1024).decode()
            print(data)

            if input("Do you want to continue? (y/n): ").lower() != 'y':
                break

        s.close()

if __name__ == '__main__':
    main()