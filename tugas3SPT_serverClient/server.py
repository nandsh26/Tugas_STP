import socket # import module socket

# socket adalah sebuah endpoint yang memungkinkan komunikasi melalui jaringan protokol jaringan seperti TCP dan UTP
# socket ini bisa digunakan untuk membangun aplikasi jaringan seperti web server, aplikasi chatting, atau game online
# server bertugas untuk menunggu koneksi dari client, mendengarkan pada port tertentu dan menunggu client yang ingin berkomunikasi
# client bertugas untuk menghubungi server pada port tertentu dan memulai komunikasi

# TCP adalah sebuah protokol yang berorientasi pada koneksi, artinya koneksi harus dibangun terlebih dahulu sebelum data dikirim
# TCP memastikan data dikirim dengan urutan yang benar dan diterima secara utuh
# sedangkan UDP adalah protokol yang tidak berorientasi pada koneksi, sehingga lebih cepat namun tidak menjamin urutan data

# membuat objek socket dengan menggunakan IPv4 dan TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# mengikat alamat IP dan port ke socket agar bisa diakses oleh client
server_socket.bind(('localhost', 8080))

# membuat server dapat mendengarkan koneksi yang masuk
# angka 5 menunjukkan jumlah maksimum koneksi yang dapat diterima dalam antrian
server_socket.listen(5)
print("Server mendengarkan informasi dari port 8080")

# menerima koneksi dari client
# fungsi accept() akan menunggu sampai ada client yang terhubung ke server
client_socket, addr = server_socket.accept()
print(f"Koneksi dari {addr} berhasil dibuat.")

# menerima data dari client
data = client_socket.recv(1024).decode()
print(f"Menerima pesan dari client: {data}")

# mengirimkan balasan ke client
client_socket.send("Hello Saya dari server!".encode())
print("Pesan telah dikirim ke client!")

# menutup koneksi dengan client
client_socket.close()

# menutup server socket setelah selesai digunakan
server_socket.close()
print("Server socket telah ditutup!")
