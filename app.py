from views.main_menu import Main_menu

def main():
    while True:
        Main_menu.write_out()  # Display the main menu
        choice = input("Vyber možnost (1-4): ").strip()
        Main_menu.handle_choice(choice)  # Handle the user's choice


if __name__ == "__main__":
    main()
