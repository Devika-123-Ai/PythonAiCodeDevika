def login(username, password):
    valid_users = {
        "admin": "password123",
        "aitesting": "python123",
        "aisecurity": "durgasoft"
    }

    return valid_users.get(username) == password
