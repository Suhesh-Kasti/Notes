import hashlib
import requests

def hash_password(password):
    # Hash the password using SHA-1
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    # Split the hash into prefix (first 5 chars) and suffix (remaining)
    print(sha1_hash)
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    return prefix, suffix

def check_password_breach(password):
    prefix, suffix = hash_password(password)

    # Query the Have I Been Pwned API with the prefix
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    
    
    if response.status_code != 200:
        print("Error fetching data from the server.")
        return

    # Response contains all suffixes starting with the prefix
    hashes = (line.split(':') for line in response.text.splitlines())
    print(hashes)
    
    # Check if the suffix is in the list
    for h, a in hashes:
        if h == suffix:
            print(f"Password found in breaches {a} times!")
            return

    print("Password not found in any known breaches.")

# Example usage
password = input("Enter your password: ")
check_password_breach(password)
