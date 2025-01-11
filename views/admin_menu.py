class AdminMenu:
    @staticmethod
    def display_menu():
        print("\nAdmin menu:")
        username = input("Username: ")
        password = input("Password: ")
        
        if username == "admin" and password == "password":
            print("SUCCESS!")
            print("Tabulka prodejů:")
        else:
            print("Neplatné údaje.")
