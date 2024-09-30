# config.py
USER_CREDENTIALS = {
    "qwerty": "qwerty",
    "user2": "password2"
}

# Function to hash a password
def hash_password(password):
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()
