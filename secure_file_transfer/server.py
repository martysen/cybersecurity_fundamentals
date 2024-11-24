'''
Entire program overview:
write server code [X]
create configuration file for openssl.cnf [X]
use .cnf file to generate server's public certificate and private keys [X]
write client code  --> make a request for file transfer from server, securely. 
run the server first in a separate terminal and then run the client in a separate terminal 
'''
import socket
import ssl

'''
server logic 
1. function := implement the server - create the socket/port; bind server to that socket; and make it listen
to requests 
2. main function: run the server :- ip addr, port, security stuff: server.crt {publicK}, server.key {privateKey}
'''

# function to establish secure server 
def start_secure_server(server_address, certfile, keyfile):
  # create a socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # secure the socket with SSL/TLS protocol
  context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
  context.load_cert_chain(certfile=certfile, keyfile=keyfile)
  secure_sock = context.wrap_socket(sock, server_side=True)

  # bind and listen to requests from clients 
  secure_sock.bind(server_address)
  secure_sock.listen(1)
  print(f"Secure Server has been started on {server_address}")

  # handle the client request once it is recieved
  while True:
    conn, addr = secure_sock.accept()
    print(f"Connection from {addr}")

    filename = conn.recv(1024).decode()
    print(f"Requested file by the client is: {filename}")

    try:
      with open(filename, 'rb') as file:
        data = file.read()
        conn.sendall(data)
      print(f"Server has sent the file: {filename}")
    except FileNotFoundError:
      conn.send(b"File not found. Try with a valid file...")
      print("File not found!!")

    conn.close()


# main function to run the server 
if __name__ == "__main__":
  server_address = ('localhost', 8443)
  certfile = 'server.crt'
  keyfile = 'server.key'
  # use the info above to call the secure server establishment function
  start_secure_server(server_address, certfile, keyfile)
