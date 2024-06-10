import socket
import threading

HOST = '127.0.0.1' 
PORT = 6666        

accounts = {
    'Hanan': {'balance': 5000},
    'Rama': {'balance': 1500}}

def handle_client(client_socket, address):
    """Handles individual client connections."""
    print(f"New connection from {address}")
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            
            request = data.split('|')
            username = request[0]
            operation = request[1]
            amount = int(request[2]) if len(request) > 2 else 0

            if username not in accounts:
                client_socket.sendall("Invalid username".encode())
            else:
                account = accounts[username]
                if operation == 'balance':
                    client_socket.sendall(f"Your balance is: {account['balance']}".encode())
                elif operation == 'deposit':
                    account['balance'] += amount
                    client_socket.sendall(f"Deposit successful. New balance: {account['balance']}".encode())
                elif operation == 'withdraw':
                    if amount > account['balance']:
                        client_socket.sendall("Insufficient funds".encode())
                    else:
                        account['balance'] -= amount
                        client_socket.sendall(f"Withdrawal successful. New balance: {account['balance']}".encode())
                else:
                    client_socket.sendall("Invalid operation".encode())

        except Exception as e:
            print(f"Error handling client: {e}")
            break

    client_socket.close()
    print(f"Connection closed with {address}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server started on {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()