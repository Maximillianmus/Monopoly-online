import queue
import socket


def connection(send_queue, receive_queue, host, port=4000):
    # instantiate
    client_socket = socket.socket()
    # connect to the server
    client_socket.connect((host, port))

    # This will get the seed and id
    data = client_socket.recv(1024).decode()
    print("SERVER:"+data)
    receive_queue.put(data)


    while True:

        message = send_queue.get()

        if message == "END":
            break

        # sends message
        print("CLIENT:" +message)
        client_socket.send(message.encode())

        # Waits for data from server and puts it in the receive_queue.
        data = client_socket.recv(1024).decode()

        print("SERVER:" + data)
        receive_queue.put(data)

        if data == "1" or data == "2":
            break

    # close the connection
    client_socket.close()
    print("User closed connection")
