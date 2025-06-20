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
