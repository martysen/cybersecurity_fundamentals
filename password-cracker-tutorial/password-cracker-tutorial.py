import hashlib
import itertools

'''
function: compute the hashes of our pwd SHA-256
function: perform the brute force attack 
function: perform the dictionary table attack 
main function: 
-- ui - pwd to crack 
-- menu: 1 (bruteforce function) or 2 (dict attack)
-- if menu 1: length the pwd 
-- if menu 2: filepath to the dictionary (./rockyou.txt)
return true or false
outer: for 1 : 1 to 10: N
inner  for 2: 1 to 5: N
inner for loops runs five times for each iteration of the outer for loop
1:1,5; 2:1,5....
N^2
32gb i7 3.2 ghz gpu nvidia 1050 ti
'''

def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()

def brute_force_crack(hash, max_length):
  chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
  for length in range(1, max_length+1):
    for guess in itertools.product(chars, repeat=length):
      guess = ''.join(guess)
      if hash_password(guess) == hash:
        return guess
  return None


def dictionary_crack(hash, dictionary_file):
  # read the dictionary file
  with open(dictionary_file, 'r') as f:
    for line in f:
      word = line.strip()
      if hash_password(word) == hash:
        return word
  return None
  

if __name__ == "__main__":
  # ask the user for the plaintext password to crack ~ simulation of pwd storage in a file or db
  hash_to_crack = input("Enter the plaintext password you want to crack: ")
  # call compute hash here
  hash_to_crack = hash_password(hash_to_crack)
  print(f"The computed hash of the input using SHA-256 is: {hash_to_crack}")
  # provide menu on how to attack
  print("Enter 1 for Brute force attack ")
  print("Enter 2 for dictionary attack ")
  choice = input("Select your option (1 or 2)")

  # ask for additional input depending on user choice of attack
  if choice == '1':
    max_length = int(input("Enter the max length of your password input"))
    result = brute_force_crack(hash_to_crack, max_length)
    if result:
      print(f"Password found: {result}")
    else:
      print("Password was not found")
  elif choice == '2':
    dictionary_file = input("Enter the filepath of the dictionary you want to use...")
    result = dictionary_crack(hash_to_crack, dictionary_file)
    if result:
      print(f"Password found: {result}")
    else:
      print("Password was not found")
  else:
    print("You have entered an invalid choice!")
