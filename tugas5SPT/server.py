import socket # untuk komunikasi jaringan
import threading # untuk menangani multiple client secara bersamaan

HOST = '127.0.0.1'  # alamat IP lokal
PORT = 12345        # port komunikasi

# Mengirim pesan ke semua client yang terhubung
def broadcast(message, clients, sender_conn=None):
    for client in clients:
        # memastikan pesan tidak dikirim kembali ke pengirim
        if client != sender_conn:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

# Menangani komunikasi dengan client
def handle_client(conn, addr, clients):
    print(f"Connected by {addr}")
    while True:
        try:
            message = conn.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Client {addr}: {message}") # menampilkan pesan di server
            broadcast(f"Client {addr}: {message}", clients, conn) # Mengirim pesan ke semua client
        except:
            break

    conn.close()
    clients.remove(conn)
    print(f"Connection closed {addr}")

# Menangani input dari server
def handle_server_input(clients):
    while True:
        message = input("") # input dari server
        broadcast(f"Server: {message}", clients)

# Setup server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f"Server started on {HOST}:{PORT}")

clients = []

# Thread khusus untuk input server
threading.Thread(target=handle_server_input, args=(clients,), daemon=True).start()

# Loop utama untuk menerima client
while True:
    conn, addr = server.accept()
    clients.append(conn)
    thread = threading.Thread(target=handle_client, args=(conn, addr, clients))
    thread.start()