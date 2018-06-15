import bluetooth

# import pickle

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print("[Checkpoint] Bluetooth ready!")

port = 1
server_sock.bind(("", port))
while True:
    server_sock.listen(1)
    print("[Checkpoint] Waiting for connection on RFCOMM channel 1...")

    # connect with  client
    client_sock, address = server_sock.accept()
    print("[Checkpoint] Accepted connection from " + address)
    client_sock.close()