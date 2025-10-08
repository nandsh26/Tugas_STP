import socket # import module socket

# TCP adalah sebuah protokol yang berorientasi pada koneksi, yang berarti koneksi harus dibangun antara 2 perangkat sebelum data ditransfer
# TCP memastikan data diunduh terlebih dahulu,data akan diterima sampai sempurna kemudian nanti akan dijalankan 
# UDP adalah sebuah protokol yang tidak berorientasi pada koneksi, yang berarti data dapat dikirim tanpa hatus membangun koneksi terlebih dahulu antara server dan client
# UDP lebih ringan dan lebih cepat, namun tidak menjamin reabilitas atau pengurutan data sesuai dengan pengirimannya

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 8080)) # hubungkan ke server

    # mengirim data ke server
    client_socket.send("Hello Saya dari client!".encode('utf-8'))

    # menerima data dari server
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Menerima pesan dari server: {data}")

    client_socket.close()

# membuat module main entry point
if __name__ == "__main__":
    start_client()