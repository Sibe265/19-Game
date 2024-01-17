import hashlib

password = "John123"

hashed_password = hashlib.sha256(password.encode()).hexdigest()

print(hashed_password)