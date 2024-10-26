'''
0. import the neccessary  dependencies required to implement the following
1. generating the public and private keys and storing them in some file
2. sign the message - phase 1 of digital signature verification scheme 
3. verify the signed message - phase 2 of the digital signature verification scheme 
'''

# import statements
# RSA crypto functions, padding schemes for secure msg encoding 
from cryptography.hazmat.primitives.asymmetric import rsa, padding
# hashing algorithms - SHA-256: to hash the msg before signing 
from cryptography.hazmat.primitives import hashes
# convert the keys to or from byte formats for storage purposes
from cryptography.hazmat.primitives import serialization
# specify who will securely implement these processes that are involved
from cryptography.hazmat.backends import default_backend

# main logic of the program 
# 2^16 + 1: 65537; 2048 bits; backend 
def generate_keys():
  private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
  public_key = private_key.public_key()

  # file input output to save the public and private key pair 
  with open("private_key.pem", 'wb') as f:
    f.write(private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption()))

  # save the public key in a file
  with open("public_key.pem", "wb") as f:
    f.write(public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))

def sign_file(filename):
  with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())

  with open(filename, "rb") as f:
    file_data = f.read()
  
  # sign the file using RSA + PSS padding + SHA-256 (MGF1) hash algo + salt 
  signature = private_key.sign(file_data, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())

  # save the generated signature in line 40
  with open("signature.sig", "wb") as f:
    f.write(signature) 
  print("File has been signed successfully...")

def verify_signature(filename):
  with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read(), backend=default_backend())
  
  with open(filename, "rb") as f:
    file_data = f.read()
  
  with open("signature.sig", "rb") as f:
    signature = f.read()

  # verify the signature 
  try: 
    public_key.verify(signature, file_data, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length = padding.PSS.MAX_LENGTH), hashes.SHA256())
    print("Signature is valid...")
  except:
    print("Signature is not valid...")

if __name__ == "__main__":
  generate_keys()
  sign_file('testfile.txt')
  verify_signature('testfile.txt')
  



