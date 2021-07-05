# Add Salting & Iterations to your hashes
import hashlib
import os

text = input("Enter String data: ")

text = text.encode()
salt = os.urandom(16)
hashed_text = hashlib.pbkdf2_hmac("sha256", text, salt, 100)

print("Text: ", text)
print("\nHashed Text (Applied salt and iterated 100 times): ", hashed_text.hex())