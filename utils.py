# utils.py
import hashlib

def generate_hash(amount, category, date):
    """Generate a SHA-256 hash for expense verification."""
    hash_input = f"{amount}{category}{date}".encode()
    return hashlib.sha256(hash_input).hexdigest()
