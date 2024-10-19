# import the brcypt library for this program
import bcrypt


'''
main function [
  while loop:
menu: 1. register,2. authentication,3. exit the program
]
func for option1: register 
func for option2: authentication
password123
a,z = 97 98
A = 65
UTF-32: 4 bytes
UTF-8==> 1byte to 4 byte 1 byte -- 8 bits
file.text => def
class Students{
  def gpa() 
  def addres() 
}
instantiate an object of Students and name it abc
abc.gpa()

'''

def register_user(username, password):
  # generate the salt
  salt = bcrypt.gensalt()
  hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
  with open('users.txt', 'a') as f:
    f.write(f"{username},{hashed_password.decode('utf-8')},{salt.decode('utf-8')}\n")
    # do not forget to the close the connection with file
  print("User registered successfully!!!")

  

def authenticate_user(username, password):
  with open('users.txt', 'r') as f:
    for line in f.readlines():
      stored_username, stored_hashed_password, stored_salt = line.strip().split(',')
      if stored_username == username:
        if bcrypt.hashpw(password.encode('utf-8'), stored_salt.encode('utf-8')) == stored_hashed_password.encode('utf-8'):
          print("Authentication was successful!!")
          return True
        else:
          print("Invalid Password")
          return False
      print("Username not found")
      return False
      # don;t forget to close the file connnection
  

def main():
  # give a welcome prompt 
  print("Mock Digital Password Storage and Authentication Demo")
  # start a infinite while loop
  while True:
    # provide the menu options
    print("\n1. Register (Input 1)")
    print("2. Authenticate (Input 2)")
    print("3. Exit the program (Input 3)")
    choice = input("Choose your option (1,2, or 3)")

    # check the input option and execute the relevant code
    if choice == '1':
      username = input("Enter your username: ")
      password = input("Enter your password: ")
      # call the function that will perform the user registration
      register_user(username, password)
    elif choice == '2':
      username = input("Enter your username: ")
      password = input("Enter your password: ")
      # call the function that will perform the user registration
      authenticate_user(username, password)
    elif choice == '3':
      break
    else:
      print("Invalid menu option. Please input either 1, 2, or 3")

# set to main
if __name__ == "__main__":
  main()