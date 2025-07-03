from cryptography.fernet import Fernet
from functools import wraps
from flask import Flask, session, render_template, redirect, request, flash

key = b'n5v05xDiKKJFAk85gExEZdlc5noDDsvZKpdlj5kNCmY='
cipher = Fernet(key)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)   
    return decorated_function


def decrypt_password(encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()

def encrypt_password(password):
    return cipher.encrypt(password.encode()).decode()