import hashlib
import sys
import os
import string
import itertools
import requests
from threading import Thread

# Detect hash type based on length
HASH_TYPES = {
    32: 'md5',
    40: 'sha1',
    64: 'sha256',
    128: 'sha512'
}

def detect_hash_type(hash_str):
    return HASH_TYPES.get(len(hash_str), None)

def generate_hash(password, hash_type):
    password = password.encode()
    if hash_type == 'md5':
        return hashlib.md5(password).hexdigest()
    elif hash_type == 'sha1':
        return hashlib.sha1(password).hexdigest()
    elif hash_type == 'sha256':
        return hashlib.sha256(password).hexdigest()
    elif hash_type == 'sha512':
        return hashlib.sha512(password).hexdigest()
    return None

# =======================
# LOAD WORDLIST FLEXIBLY
# =======================
def load_wordlist(source):
    if source.startswith("http://") or source.startswith("https://"):
        return fetch_wordlist_from_url(source)
    elif os.path.exists(source):
        return load_wordlist_from_file(source)
    else:
        print(f"[-] Wordlist not found: {source}")
        return []

def fetch_wordlist_from_url(url):
    print(f"[*] Fetching wordlist from: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.splitlines()
    except Exception as e:
        print(f"[!] Failed to fetch wordlist: {e}")
        return []

def load_wordlist_from_file(path):
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.readlines()
    except Exception as e:
        print(f"[!] Failed to load file: {e}")
        return []

# ==========================
# MULTITHREADED DICTIONARY
# ==========================
def threaded_dictionary_attack(target_hash, lines, hash_type, num_threads=4):
    def worker(passwords):
        for password in passwords:
            password = password.strip()
            hashed = generate_hash(password, hash_type)
            if hashed == target_hash:
                print(f"[✅] Password found: {password}")
                os._exit(0)  # Kill all threads
        print("[*] Thread finished.")

    chunk_size = len(lines) // num_threads
    threads = []

    for i in range(num_threads):
        chunk = lines[i * chunk_size : (i + 1) * chunk_size] if i < num_threads - 1 else lines[i * chunk_size :]
        t = Thread(target=worker, args=(chunk,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("[-] Password not found in dictionary.")

# =================
# BRUTE FORCE MODE
# =================
def brute_force_attack(target_hash, hash_type, max_length=4):
    chars = string.ascii_lowercase + string.digits
    print(f"[!] Starting brute-force (max length: {max_length})")

    for length in range(1, max_length + 1):
        for candidate in itertools.product(chars, repeat=length):
            password = ''.join(candidate)
            hashed = generate_hash(password, hash_type)
            if hashed == target_hash:
                print(f"[✅] Brute-force found: {password}")
                return
    print("[-] Brute-force failed.")

# ===================
# API Lookup Placeholder
# ===================
def online_lookup_placeholder(hash_value):
    print("[*] Placeholder for online hash API lookup.")
    print("    (e.g. hashes.com or md5decrypt.net with cookies/api)\n")

# ============
# MAIN DRIVER
# ============
def main():
    if len(sys.argv) < 3:
        print(f"Usage: python {sys.argv[0]} <hash> <wordlist_file_or_url> [--brute <max_len>]")
        sys.exit(1)

    target_hash = sys.argv[1].lower()
    wordlist_source = sys.argv[2]
    brute_force = '--brute' in sys.argv
    max_len = 4

    if brute_force:
        try:
            max_len = int(sys.argv[sys.argv.index('--brute') + 1])
        except:
            pass

    hash_type = detect_hash_type(target_hash)
    if not hash_type:
        print("[-] Unknown or unsupported hash format.")
        return

    print(f"[+] Hash type detected: {hash_type.upper()}")
    print("[+] Loading wordlist...")

    wordlist = load_wordlist(wordlist_source)
    if not wordlist:
        return

    print(f"[+] Loaded {len(wordlist)} words.\n[*] Starting dictionary attack...\n")
    threaded_dictionary_attack(target_hash, wordlist, hash_type)

    if brute_force:
        print("\n[+] Trying brute-force attack...")
        brute_force_attack(target_hash, hash_type, max_length=max_len)

    print("\n[+] Optionally, you can extend this with API-based lookups.")
    online_lookup_placeholder(target_hash)

if __name__ == "__main__":
    main()
