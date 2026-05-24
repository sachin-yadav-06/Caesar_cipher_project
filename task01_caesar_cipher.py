#!/usr/bin/env python3
"""
Task-01: Caesar Cipher
Prodigy Infotech Cybersecurity Internship
Encrypt and decrypt text using the Caesar Cipher algorithm.
"""

def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypt text using Caesar Cipher with given shift."""
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted = chr((ord(char) - base + shift) % 26 + base)
            result.append(encrypted)
        else:
            result.append(char)
    return ''.join(result)


def caesar_decrypt(text: str, shift: int) -> str:
    """Decrypt text using Caesar Cipher with given shift."""
    return caesar_encrypt(text, -shift)


def brute_force(ciphertext: str) -> None:
    """Try all 26 possible shifts and display results."""
    print("\n[*] Brute Force - All Possible Decryptions:")
    print("-" * 50)
    for shift in range(1, 27):
        decrypted = caesar_decrypt(ciphertext, shift)
        print(f"  Shift {shift:2d}: {decrypted}")


def display_banner():
    banner = """
╔══════════════════════════════════════════════╗
║          CAESAR CIPHER TOOL                  ║
║    Prodigy Infotech - Cybersecurity Task 01  ║
╚══════════════════════════════════════════════╝
"""
    print(banner)


def main():
    display_banner()

    while True:
        print("\nOptions:")
        print("  [1] Encrypt a message")
        print("  [2] Decrypt a message")
        print("  [3] Brute-force decrypt (try all shifts)")
        print("  [4] Exit")

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == '1':
            message = input("Enter message to encrypt: ")
            try:
                shift = int(input("Enter shift value (1-25): "))
                if not 1 <= shift <= 25:
                    print("[!] Shift must be between 1 and 25.")
                    continue
            except ValueError:
                print("[!] Invalid shift value.")
                continue

            encrypted = caesar_encrypt(message, shift)
            print(f"\n[+] Original  : {message}")
            print(f"[+] Shift     : {shift}")
            print(f"[+] Encrypted : {encrypted}")

        elif choice == '2':
            message = input("Enter message to decrypt: ")
            try:
                shift = int(input("Enter shift value (1-25): "))
                if not 1 <= shift <= 25:
                    print("[!] Shift must be between 1 and 25.")
                    continue
            except ValueError:
                print("[!] Invalid shift value.")
                continue

            decrypted = caesar_decrypt(message, shift)
            print(f"\n[+] Ciphertext : {message}")
            print(f"[+] Shift      : {shift}")
            print(f"[+] Decrypted  : {decrypted}")

        elif choice == '3':
            message = input("Enter ciphertext to brute-force: ")
            brute_force(message)

        elif choice == '4':
            print("\n[*] Exiting. Goodbye!")
            break

        else:
            print("[!] Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()
