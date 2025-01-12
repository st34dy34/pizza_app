from views.main_menu import MainMenu

def main():
    print("Welcome to the Pizza Order Application!")
    main_menu = MainMenu()
    
    while True:
        main_menu.write_out()  # Display the main menu options
        choice = input("Choose an option (1-4): ").strip()
        main_menu.handle_choice(choice)  # Handle user input

if __name__ == "__main__":
    main()
