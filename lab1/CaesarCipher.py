def encrypt_caesar(plaintext):
    result = ""
    shift = 3  # Caesar cipher shifts characters by 3 positions
    
    for char in plaintext:
        if char.isalpha():
            # Handle uppercase letters (A-Z)
            shifted = ord(char) + shift
            if shifted > ord('Z'):
                shifted -= 26  # Wrap around if it goes beyond 'Z'
            result += chr(shifted)
        else:
            result += char  # Non-alphabetic characters remain unchanged

    return result

def decrypt_caesar(ciphertext):
    result = ""
    shift = 3  # Caesar cipher shifts characters by 3 positions
    
    for char in ciphertext:
        if char.isalpha():
            # Handle uppercase letters (A-Z)
            shifted = ord(char) - shift
            if shifted < ord('A'):
                shifted += 26  # Wrap around if it goes beyond 'A'
            result += chr(shifted)
        else:
            result += char  # Non-alphabetic characters remain unchanged

    return result

if __name__ == "__main__":
    print(encrypt_caesar("PYTHON"))  
    print(decrypt_caesar("SBWKRQ"))  
