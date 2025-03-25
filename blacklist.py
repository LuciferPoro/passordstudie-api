# blacklist.py
blacklisted_passwords = {
    "123456", "password", "qwerty", "abc123", "admin", "letmein", "welcome"
}

def is_blacklisted(password):
    return password.lower() in blacklisted_passwords
