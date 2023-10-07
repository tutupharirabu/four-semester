# Import modul soket
import socket

def tcp_server():
    # Menyiapkan soket server
    SERVER_HOST = "127.0.0.1"
    SERVER_PORT = 8080

    # Membuat objek soket TCP
    sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Mengikat soket ke alamat dan port tertentut
    sock_server.bind((SERVER_HOST, SERVER_PORT))

    # Melakukan listen pada koneksi masuk
    sock_server.listen(1)

    print('Server is ready to serve....')

    while True:
        # Membangun koneksi
        sock_client, client_address = sock_server.accept()

        # Menerima permintaan klien
        request = sock_client.recv(1024).decode()
        print("Dari Client :"+request)

        # Men-handle request dan mendapatkan respons
        response = handle_request()
        
        # Mengirim respons ke klien
        sock_client.send(response.encode())

        # Menutup soket klien
        sock_client.close()
    # Endwhile

    # Menutup soket server
    sock_server.close()

def handle_request():
    try:
        CSS_FILE = "style.css"
        JS_FILE = "script.js"

        # Memuat file HTML
        file = open("index.html", 'rb')
        message_body = file.read()
        file.close()

        # Memuat file CSS
        css_file = open(CSS_FILE, 'rb')
        css_content = css_file.read()
        css_file.close()

        # Memuat file JS
        js_file = open(JS_FILE, 'rb')
        js_content = js_file.read()
        js_file.close()
 
        response_line = "HTTP/1.1 200 OK\r\n"
        content_type = "Content-Type: text/html\r\n\r\n"
        response_body = message_body.decode() + "<style>" + css_content.decode() + "</style>"
        response_body += "<script>" + js_content.decode() + "</script>"

        response = response_line + content_type + response_body

    except FileNotFoundError:
        # Apabila File tidak ditemukan, maka return "404 Not Found response"
        response_line = "HTTP/1.1 404 Not Found\r\n"
        content_type = "Content-Type: text/html\r\n\r\n"
        response_body = "<h1>404 Not Found</h1><p>The requested file was not found on this server.</p>"
        response = response_line + content_type + response_body

    return response

if __name__ == "__main__":
    tcp_server()