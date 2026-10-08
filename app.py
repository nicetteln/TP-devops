def hello(name):
    return f"Bienvenue {name} (login)"

def login(user, password):
    return user == "admin" and password == "1234"

if __name__ == "__main__":
    print(hello("monde"))
