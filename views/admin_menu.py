class AdminMenu:
    def authenticate(self):
        print("\n--- Admin Login ---")
        username = input("Username: ")
        password = input("Password: ")
        
        if username == "admin" and password == "password":
            print("Login successful!")
            return True
        else:
            print("Invalid credentials.")
            return False