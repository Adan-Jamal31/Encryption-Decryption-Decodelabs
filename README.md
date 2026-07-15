# Project 2: Basic Encryption & Decryption (Caesar Cipher)

## DecodeLabs Cyber Security Internship

This repository contains my implementation of **Project 2** for the DecodeLabs Cyber Security Internship. The project demonstrates how the Caesar Cipher algorithm encrypts and decrypts text using a user-defined shift key.

---

# Project Overview

- **Goal:** Implement a simple encryption and decryption program using the Caesar Cipher algorithm.
- **Cipher:** Caesar Cipher (Shift Cipher)
- **Language:** Python
- **Concepts Covered:** Cryptography, Encryption, Decryption, String Manipulation

---

# Features

- Encrypts user-entered text.
- Decrypts encrypted text back to the original message.
- Supports uppercase and lowercase letters.
- Preserves spaces, numbers, and special characters.
- Uses a user-defined shift key.

---

# How It Works (The Mathematics)

The Caesar Cipher shifts every alphabetic character by a fixed number of positions.

### Encryption Formula

\[
E(x) = (x + n) \bmod 26
\]

### Decryption Formula

\[
D(x) = (x - n) \bmod 26
\]

Where:

- **x** = Position of the letter
- **n** = Shift key
- **26** = Total letters in the English alphabet

---

# File Structure

```
Basic-Encryption-Decryption-Decodelabs/
│
├── caesar_cipher.py
└── README.md
```

---

# How to Run

Open a terminal and execute:

```bash
python3 caesar_cipher.py
```

---

# Example

### Input

```
Enter your message:
Hello World

Enter shift key:
3
```

### Output

```
Original Message : Hello World

Encrypted Message : Khoor Zruog

Decrypted Message : Hello World
```

---

# Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

---

# Learning Outcomes

- Understand the fundamentals of classical cryptography.
- Learn how encryption and decryption work.
- Improve Python programming skills.
- Gain practical experience with GitHub.

---

DecodeLabs Cyber Security Internship – Week 2 Project
