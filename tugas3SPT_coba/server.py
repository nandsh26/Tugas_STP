# socket adalah sebuah endpoint yang memungkinkan komunikasi melalui jaringan protokol jaringan seperti TCP dan UTP
# socket ini bisa digunakan untuk membangun aplikasi jaringan seperti web server, aplikasi chatting atau game online
# server bertugas untuk menunggu koneksi dari client, mendengarkan pada port tertentu dan menunggu client yang ingin berkomunikasi
# client bertugas untuk menghubungi server pada port tertentu dan memulai komunikasi

# TCP akan menyediaan sebuah komunikasi yang handal dan terurut, memastikan data yang dikirim akan diterima dengan benar dan sesuai dengan urutannya
# UDP adalah sebuah model protokol yang lebih ringan dan lebih cepat, namun tidak menjamin data yang dikirim akan diterima dengan urutan yang benar

import socket # import module socket

# membuat fungsi untuk memulai server
def start_server() -> None: # returnnya dari nol

    # membuat socket dengan IPv4 dan TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # mengikat soket ke alamat IP dan port
    server_socket.bind(("localhost", 8080))

    # membuat server dapat mendengar koneksi yang masuk
    server_socket.listen(5) # angka 5 menunjukkan jumlah maksimum koneksi yang dapat diterima dalam antrian
    print("Server mendengarkan informasi dari port 8080")

    # looping untuk menjalankan versi dari server socketnya
    while True:

        # menerima koneksi dari client
        client_socket, client_address = server_socket.accept() # accept() akan menerima koneksi dari client yang akan mengembalikan socket baru dan alamat IP dari client yang akan terhubung ke server
        print(f"Connection from {client_address} has been established!")

        # menerima data dari client
        data = client_socket.recv(1024).decode('utf-8') # fungsi recv() akan menerima data dari client dengan maksimal 1024 byte yang dapat diterima dalam satu kali panggilan
        print(f"Menerima pesan dari client: {data}")

        # mengirim balasan ke client
        client_socket.send("Hello dari server!".encode('utf-8'))

        # menutup koneksi dengan client
        client_socket.close()

# membuat module main entry point
if __name__ == "__main__":
    start_server()