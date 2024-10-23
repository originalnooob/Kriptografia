"""
File: crypto.py
---------------
Assignment 1: Cryptography
Course: CS 41
Name: <KANTOR JANOS>
SUNet: <kjim2243>

"""



# Caesar Cipher Functions

def encrypt_caesar(plaintext):
    encrypted = []
    for char in plaintext:
        if char.isalpha():
            shifted = (ord(char) - ord('A') + 3) % 26 + ord('A')
            encrypted.append(chr(shifted))
        else:
            encrypted.append(char)
    return ''.join(encrypted)


def decrypt_caesar(ciphertext):
    decrypted = []
    for char in ciphertext:
        if char.isalpha():
            shifted = (ord(char) - ord('A') - 3) % 26 + ord('A')
            decrypted.append(chr(shifted))
        else:
            decrypted.append(char)
    return ''.join(decrypted)

#Vigenere Cipher Function
def encrypt_vigenere(plaintext, keyword):
    keyword_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]
    encrypted = []
    for p, k in zip(plaintext, keyword_repeated):
        shift = ord(k) - ord('A')
        shifted = (ord(p) - ord('A') + shift) % 26 + ord('A')
        encrypted.append(chr(shifted))
    return ''.join(encrypted)


def decrypt_vigenere(ciphertext, keyword):
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]
    decrypted = []
    for c, k in zip(ciphertext, keyword_repeated):
        shift = ord(k) - ord('A')
        shifted = (ord(c) - ord('A') - shift) % 26 + ord('A')
        decrypted.append(chr(shifted))
    return ''.join(decrypted)


# Completed Merkle-Hellman Knapsack Cryptosystem Functions

import random
from utils import coprime, byte_to_bits, modinv, bits_to_byte

def generate_private_key(n=8):
    """Generate a private key for use in the Merkle-Hellman Knapsack Cryptosystem."""
    w = [random.randint(2, 10)]
    while len(w) < n:
        total = sum(w)
        w.append(random.randint(total + 1, 2 * total))
    
    q = random.randint(sum(w) + 1, 2 * sum(w))
    r = random.randint(2, q - 1)
    while not coprime(r, q):
        r = random.randint(2, q - 1)
    
    return tuple(w), q, r

def create_public_key(private_key):
    """Creates a public key corresponding to the given private key."""
    w, q, r = private_key
    beta = tuple((r * wi) % q for wi in w)
    return beta

def encrypt_mh(message, public_key):
    """Encrypt an outgoing message using a public key."""
    encrypted = []
    for byte in message:
        bits = byte_to_bits(ord(byte))
        c = sum(bi * ai for bi, ai in zip(public_key, bits))
        encrypted.append(c)
    return encrypted

def decrypt_mh(ciphertext, private_key):
    """Decrypt an incoming message using a private key."""
    w, q, r = private_key
    s = modinv(r, q)
    
    decrypted = []
    for c in ciphertext:
        c_prime = (c * s) % q
        bits = []
        for wi in reversed(w):
            if wi <= c_prime:
                bits.append(1)
                c_prime -= wi
            else:
                bits.append(0)
        bits.reverse()
        decrypted.append(chr(bits_to_byte(bits)))
    
    return ''.join(decrypted)

