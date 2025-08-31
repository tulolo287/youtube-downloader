import socket
import ssl

def vpn_client(server_ip='127.0.0.1', port=1194):
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations(cafile="server.crt")

    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    secure_socket = context.wrap_socket(raw_socket, server_hostname=server_ip)

    try:
        secure_socket.connect((server_ip, port))
        print(f"Подключен к VPN серверу {server_ip}:{port}")

        while True:
            data = input("Введите сообщение: ").encode('utf-8')
            secure_socket.sendall(data)
            response = secure_socket.recv(4096)
            print(f"Ответ от сервера: {response.decode('utf-8')}")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        secure_socket.close()

if __name__ == '__main__':
    vpn_client()
