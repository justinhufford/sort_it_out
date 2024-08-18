import config
import display

def modify_settings():
    while True:
        display.clear()
        display.logo()
        print(f"[1] List Length: {config.settings['list_length']}")
        print(f"[2] Random Number Upper Limit: {config.settings['random_number_upper_limit']}")
        print(f"[3] Animation and Enhancements: {'On' if config.settings['enable_animation'] else 'Off'}")
        print("[0] Back")

        choice = input("\n> ")

        if choice == "1":
            display.clear()
            try:
                new_list_length = int(input("Enter new list length: "))
                config.settings["list_length"] = new_list_length
                config.save_settings()
            except ValueError:
                print("Invalid input. List length not changed.")
            
        elif choice == "2":
            display.clear()
            try:
                new_upper_limit = int(input("Enter new random number upper limit: "))
                config.settings["random_number_upper_limit"] = new_upper_limit
                config.save_settings()
            except ValueError:
                print("Invalid input. Upper limit not changed.")

        elif choice == "3":
            config.settings["enable_animation"] = not config.settings["enable_animation"]
            config.save_settings
        
        elif choice == "0":
            display.clear()
            break
        else:
            print("Invalid choice. Please select again.")

