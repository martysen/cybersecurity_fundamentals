import socket
import ssl

'''
function to establish conn with server / secure
main function to fire the client 
'''

def download_file(server_address, filename):
  # create a socket 
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # wrap the socket with security SSL/TLS
  context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
  context.load_verify_locations('server.crt') # verify the server certi
  secure_sock = context.wrap_socket(sock, server_hostname=server_address[0])

  # establish connection with server and send file request 
  secure_sock.connect(server_address)
  secure_sock.sendall(filename.encode())

  # receive server response (with data)
  with open(f"downloaded_{filename}", 'wb') as file:
    while True: 
      data = secure_sock.recv(1024)
      if not data: 
        break
      file.write(data)
  
  print(f"Downloaded file successfully. for file {filename}")
  secure_sock.close()



if __name__ == "__main__":
  server_address = ('localhost', 8443)
  filename = 'textfile.txt'
  download_file(server_address, filename)
