# Write a Program in Python to generate hashes of string data using 3 algorithm from hashlib
import hashlib

# asking for input string
text = input("Enter String data: ")

#Using SHA1 Algorithm
Hash_1=hashlib.sha1(text.encode()).hexdigest()
print("Hashed Password using SHA1: ", Hash_1)

#Using BLAKE2b Algorithm
Hash_2=hashlib.blake2b(text.encode()).hexdigest()
print("Hashed Password using BLAKE2b: ", Hash_2)

#Using SHA3_224 Algorithm
Hash_3=hashlib.sha3_224(text.encode()).hexdigest()
print("Hashed password using SHA3_224: ", Hash_3)