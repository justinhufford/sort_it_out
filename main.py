import display
import gameloop
import settings

def main_menu():
    while True:
        display.clear()
        display.logo()
        print("[1] Play")
        print("[2] Settings")
        print("[0] Quit")

        choice = input("\n> ")

        if choice == "1":
            gameloop.main()
        elif choice == "2":
            settings.modify_settings()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main_menu()
