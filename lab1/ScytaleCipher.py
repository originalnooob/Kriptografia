def encrypt_scytale(plaintext, circumference):
    padded_length = len(plaintext) + (circumference - len(plaintext) % circumference) % circumference
    padded_plaintext = plaintext.ljust(padded_length)
    
    ciphertext = []
    for col in range(circumference):
        for i in range(col, len(padded_plaintext), circumference):
            ciphertext.append(padded_plaintext[i])
    
    return ''.join(ciphertext)

def decrypt_scytale(ciphertext, circumference):
    rows = len(ciphertext) // circumference
    
    plaintext = []
    for row in range(rows):
        for i in range(row, len(ciphertext), rows):
            plaintext.append(ciphertext[i])
    
    return ''.join(plaintext)

if __name__ == "__main__":
    encrypted = encrypt_scytale("IAMHURTVERYBADLYHELP", 5)
    print(encrypted)
    
    decrypted = decrypt_scytale("IRYYATBHMVAEHEDLURLP", 5)
    print(decrypted) 
