def register_user(username, email, password, role="graduate"):
    # Try to register
    r = requests.post(BASE_URL + "auth/register/", json={
        "username": username,
        "email": email,
        "password": password,
        "role": role
    })

    if r.status_code == 400:
        print(f"User {username} already exists, resetting password...")
        # Reset password via admin endpoint or Django manage.py command
        # For simplicity, we assume an endpoint exists: /auth/reset_password/
        # You can create a temporary admin-only endpoint for testing
        requests.post(BASE_URL + "auth/reset_password/", json={
            "username": username,
            "password": password
        })
    else:
        print(f"Registered {role} user {username}: ", r.status_code, r.json())

    return login_user(username, password)
