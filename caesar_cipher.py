# ==========================================
# DecodeLabs Cyber Security Internship
# Project 2: Basic Encryption & Decryption
# ==========================================

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("=== Caesar Cipher Encryption & Decryption ===")

    message = input("Enter your message: ")
    shift = int(input("Enter shift key (e.g., 3): "))

    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)

    print("\n----- Results -----")
    print("Original Message :", message)
    print("Encrypted Message:", encrypted)
    print("Decrypted Message:", decrypted)


if __name__ == "__main__":
    main()