import threading
import queue


# Handles the communication between a client and the server.
def connection(conn, address, receive_queue, send_queue, client_list: list):

    client_list.append(address)

    # Sends the ID and seed.
    first_message = send_queue.get()
    print(first_message)
    conn.send(first_message.encode())

    while True:
        # Get input from the client, puts it into receive queue
        data = conn.recv(1024).decode()
        print("Received", data)
        receive_queue.put(address)
        receive_queue.put(data)

        # Sends back information from the send queue.
        message = send_queue.get()
        print("Sent", message)
        conn.send(message.encode())


# Sets up threads for each client connecting to the server.
def handle_connections(server_socket, receive_queue, queue_list, player_list):
    while True:
        # Waits for a connection
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        # Creates a queue for that connection
        queue_list.append(queue.Queue(0))
        # Starts a connection thread for communication between that client and server
        t = threading.Thread(target=connection, args=(conn, str(address), receive_queue, queue_list[-1], player_list))
        t.setDaemon(True)
        t.start()
