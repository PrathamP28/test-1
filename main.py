# 🍃🍀  
from cryptography.fernet import Fernet
import zlib
import base64

# Generate a key (store this securely)
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_message(message: str) -> bytes:
    # Compress the message
    compressed_message = zlib.compress(message.encode())
    
    # Encrypt the compressed message
    encrypted_message = cipher.encrypt(compressed_message)
    
    return encrypted_message

def decrypt_message(encrypted_message: bytes) -> str:
    # Decrypt the message
    decrypted_compressed_message = cipher.decrypt(encrypted_message)
    
    # Decompress the message
    original_message = zlib.decompress(decrypted_compressed_message).decode()
    
    return original_message

# Example usage
message = "Hello, this is a secret message!"
encrypted = encrypt_message(message)
print("Encrypted:", base64.b64encode(encrypted).decode())  # Base64 for readability

# Decryption
decrypted = decrypt_message(encrypted)
print("Decrypted:", decrypted)
# written by Pratham 🍂🍁
