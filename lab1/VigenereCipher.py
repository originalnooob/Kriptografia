def encrypt_vigenere(plaintext, keyword):
    result = []
    keyword_repeated = extend_keyword(keyword, len(plaintext))

    for i in range(len(plaintext)):
        p = ord(plaintext[i]) - ord('A')
        k = ord(keyword_repeated[i]) - ord('A')
        encrypted_char = chr((p + k) % 26 + ord('A'))
        result.append(encrypted_char)
    
    return ''.join(result)

def decrypt_vigenere(ciphertext, keyword):
    result = []
    keyword_repeated = extend_keyword(keyword, len(ciphertext))

    for i in range(len(ciphertext)):
        c = ord(ciphertext[i]) - ord('A')
        k = ord(keyword_repeated[i]) - ord('A')
        decrypted_char = chr((c - k) % 26 + ord('A'))
        result.append(decrypted_char)
    
    return ''.join(result)

def extend_keyword(keyword, length):
    repeated_keyword = (keyword * (length // len(keyword))) + keyword[:length % len(keyword)]
    return repeated_keyword


if __name__ == "__main__":
    print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))  
    print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON")) 
