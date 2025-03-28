import socket

def start_server():
    # Configuración del servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen(5)

    print("Servidor TCP escuchando en el puerto 5000...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Cliente conectado desde {addr}")

        while True:
            message = conn.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Mensaje recibido: {message}")
            
            # Responder con "HOLA CLIENTE" si el mensaje es "HOLA SERVIDOR"
            if message.lower() == "hola servidor":
                response = "HOLA CLIENTE"
            elif message == "DESCONEXION":
                print("Desconectando cliente...")
                conn.close()
                break
            else:
                response = message.upper()

            conn.sendall(response.encode('utf-8'))

        # El servidor sigue escuchando para nuevas conexiones
        print("Servidor TCP escuchando en el puerto 5000...")

if __name__ == "__main__":
    start_server()
