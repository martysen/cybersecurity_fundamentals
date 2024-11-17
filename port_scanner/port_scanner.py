# import libraries 
import socket

'''
1. function: port scanning operation
  use the socket library - try to establish a connection with all the ports enumerated between the 
  range of the start_port and the end_port 
  if a connection was successfully establish -- report that port number 
  repeat the previous two steps until - finished scanning the range of port numbers 
2. main function: 
  user input - 3 user input: target_ip, start_port, end_port ==> store in respective variables
  call the port scanning function by passing the variable of the previous step as input to the function

'''


# define the prototype of the port scan function 
def port_scan(target_ip, start_port, end_port):
  print(f"Begin Scanning target system/network with IP address: {target_ip}")
  # start a loop that will go over one port number at a time starting from the start value till end value +1
  for port in range(start_port, end_port + 1):
    # create a socket object 
    # specify the address family ~ Internet ~ IPv4 IP address 
    # type of the socket -- protocol that is being used: TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    # attempt to connect to the port number which is specified in the current iteration of the for loop
    # if conn is successful : connect_ex returns 0 
    # if conn was unsuccessful: connect_ex return some non-zero integer 
    result = sock.connect_ex((target_ip, port))
    # capture the port with which we succesfully established a connection
    if result == 0:
      print(f"Port Number: {port} is Open...")
    sock.close()

# main function
# when you have datatype - convert it to another type - typecasting 
if __name__ == "__main__":
  target_ip = input("Enter the target IP address that you want to scan: ")
  start_port = int(input("Enter the starting port number: "))
  end_port = int(input("Enter the ending port number: "))
  port_scan(target_ip, start_port, end_port)

# test cases to use for screenshot submission {private}
# only execute on your own system or your own home network - and no where else
'''
ip: 127.0.0.1
start 1 to 1024~7000

home network: 
ip: 192.168.1.1
'''
