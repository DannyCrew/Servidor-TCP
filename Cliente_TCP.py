import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000))

    while True:
        message = input("Escribe un mensaje para enviar al servidor: ")
        client_socket.sendall(message.encode('utf-8'))

        if message.upper() == "DESCONEXION":
            print("Desconectando del servidor...")
            client_socket.close()
            break

        response = client_socket.recv(1024).decode('utf-8')
        print(f"Respuesta del servidor: {response}")

if __name__ == "__main__":
    start_client()
