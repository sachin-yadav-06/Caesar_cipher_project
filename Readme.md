# 🔐 Task 01 — Caesar Cipher
### Prodigy Infotech Cybersecurity Internship

> **Author:** Sachin Yadav

---

## 📌 Overview

The Caesar Cipher is one of the oldest and simplest encryption techniques. It works by shifting each letter in the plaintext by a fixed number of positions in the alphabet. This tool implements full **encrypt**, **decrypt**, and **brute-force** modes from the command line.

---

## 📸 Screenshots

### 🖥️ 1. Main Menu
```
╔══════════════════════════════════════════════╗
║          CAESAR CIPHER TOOL                  ║
║    Prodigy Infotech - Cybersecurity Task 01  ║
╚══════════════════════════════════════════════╝

Options:
  [1] Encrypt a message
  [2] Decrypt a message
  [3] Brute-force decrypt (try all shifts)
  [4] Exit

Enter choice (1-4): _
```
> 📷 *Screenshot: Tool banner and interactive menu on launch*

![Main Menu] <img width="750" height="347" alt="Image" src="https://github.com/user-attachments/assets/f582d90a-51a0-45d8-8ade-0f5dfc5e8596" />

---

### 🔒 2. Encrypting a Message
```
Enter choice (1-4): 1
Enter message to encrypt: Hello, Sachin Yadav!
Enter shift value (1-25): 7

[+] Original  : Hello, Sachin Yadav!
[+] Shift     : 7
[+] Encrypted : Olssv, Zhjopu Fhkha!
```
> 📷 *Screenshot: Encryption output — plaintext converted to ciphertext with shift 7*

![Encrypt Output](screenshots/task01_02_encrypt.png)

---

### 🔓 3. Decrypting with Known Key
```
Enter choice (1-4): 2
Enter message to decrypt: Olssv, Zhjopu Fhkha!
Enter shift value (1-25): 7

[+] Ciphertext : Olssv, Zhjopu Fhkha!
[+] Shift      : 7
[+] Decrypted  : Hello, Sachin Yadav!
```
> 📷 *Screenshot: Decryption restores original message using the same shift key*

![Decrypt Output](screenshots/task01_03_decrypt.png)

---

### 🔨 4. Brute Force Attack (All 26 Shifts)
```
Enter choice (1-4): 3
Enter ciphertext to brute-force: Olssv, Zhjopu Fhkha!

[*] Brute Force - All Possible Decryptions:
──────────────────────────────────────────────────
  Shift  1: Nkrru, Yginot Egjgz!
  Shift  2: Mjqqt, Xfhmns Dfife!
  Shift  3: Lipps, Weglmr Cehde!
  Shift  4: Khoor, Vdfklq Bdgcd!
  Shift  5: Jgnnq, Uejkjp Acfbc!
  Shift  6: Ifmmp, Tdijio Zbeba!
  Shift  7: Hello, Sachin Yadav!   ← ✅ Readable plaintext!
  Shift  8: Gdkkn, Rzbgm Xzczu!
  ...
  Shift 26: Olssv, Zhjopu Fhkha!  (original)
```
> 📷 *Screenshot: All 26 possible decryptions — shift 7 reveals the readable message*

![Brute Force](screenshots/task01_04_bruteforce.png)

---

## 🎯 Objectives

- Understand the fundamentals of symmetric encryption
- Implement character-level substitution using modular arithmetic
- Explore why simple ciphers are vulnerable to brute-force attacks

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| ✅ Encrypt | Convert plaintext → ciphertext with a shift key |
| ✅ Decrypt | Recover plaintext from ciphertext using the same shift |
| ✅ Brute Force | Try all 26 shifts and display every possible decryption |
| ✅ Case Preservation | Uppercase and lowercase letters handled separately |
| ✅ Non-alpha passthrough | Numbers, spaces, punctuation are left unchanged |

---

## ⚙️ Requirements

- Python 3.8+
- No external libraries — pure standard library

---

## 🚀 How to Run

```bash
python3 task01_caesar_cipher.py
```

---

## 🔬 How It Works

```
Encryption:   E(x) = (x + shift) mod 26
Decryption:   D(x) = (x - shift) mod 26

Where x = alphabetic index of the character (A=0, B=1 ... Z=25)
```

---

## 🛡️ Security Notes

- Caesar Cipher is **trivially brute-forceable** — only 25 possible keys
- Modern encryption (AES-256) has key space 2²⁵⁶ — practically uncrackable
- This demonstrates why **key space size** is fundamental to cryptographic security

---

## 📁 File Structure

```
task01_caesar_cipher.py              ← Main script
README_Task01_Caesar_Cipher.md       ← This file
screenshots/
  ├── task01_01_menu.png
  ├── task01_02_encrypt.png
  ├── task01_03_decrypt.png
  └── task01_04_bruteforce.png
```

---

## 👤 Author

| Field | Details |
|-------|---------|
| **Name** | Sachin Yadav |
| **Internship** | Prodigy Infotech — Cybersecurity |
| **Task** | 01 — Caesar Cipher |
