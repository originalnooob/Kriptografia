import json
from Crypto.Cipher import AES, DES
from Crypto.Util.Padding import pad, unpad

# Padding implementations
def apply_padding(data, block_size, padding_type):
    if padding_type == "zero-padding":
        pad_len = block_size - (len(data) % block_size)
        return data + b'\x00' * pad_len
    elif padding_type == "PKCS7":
        pad_len = block_size - (len(data) % block_size)
        return data + bytes([pad_len] * pad_len)
    elif padding_type == "Schneier-Ferguson":
        pad_len = block_size - (len(data) % block_size)
        return data + bytes([pad_len] * pad_len)
    else:
        raise ValueError("Unsupported padding type.")

def remove_padding(data, padding_type):
    if padding_type in ["PKCS7", "Schneier-Ferguson"]:
        pad_len = data[-1]
        return data[:-pad_len]
    elif padding_type == "zero-padding":
        return data.rstrip(b'\x00')
    else:
        raise ValueError("Unsupported padding type.")

# Custom Cipher implementation
class CustomCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        return bytes((b + self.key[i % len(self.key)]) % 256 for i, b in enumerate(data))

    def decrypt(self, data):
        return bytes((b - self.key[i % len(self.key)]) % 256 for i, b in enumerate(data))

# Cipher factory
def get_cipher(algorithm, key, mode, iv=None):
    if algorithm == "AES":
        mode_constant = getattr(AES, f"MODE_{mode}")
        if iv:
            return AES.new(key, mode_constant, iv)
        else:
            return AES.new(key, mode_constant)
    elif algorithm == "DES":
        mode_constant = getattr(DES, f"MODE_{mode}")
        if iv:
            return DES.new(key, mode_constant, iv)
        else:
            return DES.new(key, mode_constant)
    elif algorithm == "Custom":
        return CustomCipher(key)
    else:
        raise ValueError("Unsupported algorithm.")

# Configuration loader
def load_config(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

# File encryption
def encrypt_file(config):
    cipher = get_cipher(
        config['algorithm'], 
        bytes.fromhex(config['key']), 
        config['mode'], 
        bytes.fromhex(config['iv']) if 'iv' in config else None
    )
    with open(config['test_file'], 'rb') as infile, open(config['test_file'] + '.enc', 'wb') as outfile:
        data = infile.read()
        padded_data = apply_padding(data, config['block_size'] // 8, config['padding'])
        if isinstance(cipher, CustomCipher):
            encrypted_data = cipher.encrypt(padded_data)
        else:
            encrypted_data = cipher.encrypt(padded_data)
        outfile.write(encrypted_data)

# File decryption
def decrypt_file(config):
    cipher = get_cipher(
        config['algorithm'], 
        bytes.fromhex(config['key']), 
        config['mode'], 
        bytes.fromhex(config['iv']) if 'iv' in config else None
    )
    with open(config['test_file'] + '.enc', 'rb') as infile, open(config['test_file'] + '.dec', 'wb') as outfile:
        data = infile.read()
        if isinstance(cipher, CustomCipher):
            decrypted_data = cipher.decrypt(data)
        else:
            decrypted_data = cipher.decrypt(data)
        unpadded_data = remove_padding(decrypted_data, config['padding'])
        outfile.write(unpadded_data)

# Test runner
def run_tests():
    config = load_config('config.json')

    print("Running encryption...")
    encrypt_file(config)

    print("Running decryption...")
    decrypt_file(config)

    print("Test completed.")

# Entry point
if __name__ == "__main__":
    run_tests()