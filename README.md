# 🔐 Hash Cracker - Dictionary & Brute-Force Password Cracking Tool

A lightweight, multithreaded Python script to crack hashed passwords using dictionary attacks, remote URL wordlists, and optional brute-force techniques. Supports common hashing algorithms including MD5, SHA1, SHA256, and SHA512.

---

## ✨ Features

- 🔍 Automatic hash type detection (MD5, SHA1, SHA256, SHA512)
- 📁 Flexible wordlist input (file path or URL)
- ⚙️ Multithreaded dictionary attack for improved speed
- 🧠 Optional brute-force mode (alphanumeric with configurable length)
- 🧩 Placeholder for API-based hash lookups (e.g., hashes.com, md5decrypt.net)

---

## 🧠 How It Works

1. Detects the hash type automatically based on length.
2. Loads a wordlist from a file or a direct URL.
3. Launches a dictionary attack using multiple threads.
4. Optionally performs brute-force if `--brute` is passed.
5. Prepares for future integration with online hash-cracking APIs.

---

## ⚙️ Installation

Install the required Python dependency:

```bash
pip install requests

## 🚀 Usage
Step 1: Navigate to your script directory
cd C:\cracker

Run the script using one of the following commands:
✅ Remote wordlist (GitHub raw link):
python password.py a4bf9ecfc5fc3ab2f482aa328435a3a4 'https://raw.githubusercontent.com/nonigopalchandro/password/refs/heads/main/pass.txt'

✅ Local wordlist file:
python password.py 06e112b87f40f4520bcdb280192a2a64 passwords.txt

✅ With brute-force mode (max 4 characters):
python password.py 06e112b87f40f4520bcdb280192a2a64 passwords.txt --brute 4
Replace the hash and file path or URL as needed.

