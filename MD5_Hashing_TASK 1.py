# Write a Program in Python to generate MD5 of string data.
import hashlib

# input string
text = input("Enter String Data: ")

md5_hash = hashlib.md5(text.encode()).hexdigest()
print ("MD5: " + md5_hash)