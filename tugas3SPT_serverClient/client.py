import socket # import module socket

# client bertugas untuk menghubungi server pada alamat IP dan port tertentu
# setelah terhubung, client dapat mengirim data ke server dan menerima balasannya
# komunikasi ini dilakukan menggunakan protokol TCP agar data terkirim dengan urutan yang benar

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# menghubungkan client ke server
client_socket.connect(("localhost", 8080))
print("Client berhasil terhubung ke server!")

# mengirim data ke server
client_socket.send("Hello Saya dari client!".encode("utf-8"))
print("Pesan telah dikirim ke server!")

# menerima balasan dari server
data = client_socket.recv(1024).decode("utf-8") #utf-8 untuk mengubah byte ke string
print(f"Menerima pesan dari server: {data}")

# menutup koneksi dengan server
client_socket.close()
print("Koneksi dengan server telah berakhir!")
