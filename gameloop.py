import random
import time

import display
import config


numbered_list = []
 #  List for the player to fill in
previously_generated_numbers = []
 #  Helps ensure each random number is unique

def reset_game():
    global numbered_list, previously_generated_numbers
    numbered_list = [None] * config.settings["list_length"]
    previously_generated_numbers.clear()

def print_list():
 #  Print a numbered list with all player choices
    for index, value in enumerate(numbered_list, start=1):
        print(f"{index}. {'' if value is None else value}")
    print()

def generate_random_number():
    print()
    if config.settings.get("enable_animation", True):  # Check if rolling animation is enabled
        # Simulate rolling effect
        for _ in range(20):
            random_number = random.randint(1, config.settings["random_number_upper_limit"])
            display.clear_lines(1)  # Clear the previous number
            print(f"Number: {random_number}/{config.settings['random_number_upper_limit']}")
            time.sleep(0.05)  # Small delay to create the rolling effect
    
    # Final number
    while True:
        final_number = random.randint(1, config.settings["random_number_upper_limit"])
        if final_number not in previously_generated_numbers:
            break
    
    display.clear_lines(1)  # Clear the rolling number (if animation was used)
    print(f"Number: {final_number}/{config.settings['random_number_upper_limit']}")
    print()
    return final_number

def collect_position(): 
    instructions = "Place the number. (Type 'q' to quit.)"
    
    while True:
        print(instructions)
        user_input = input("> ").strip()

        if user_input.lower() == 'q':
            return 'q'  # Indicate that the player wants to quit

        try: 
            position = int(user_input)

            # Check if the position is within the valid range
            if position < 1 or position > config.settings["list_length"]:
                instructions = display.color_text(f"Choose a number between 1 and {config.settings['list_length']}.", 'red')
                display.clear_lines(2)
                continue
            
            # Check if the selected position is already occupied
            if numbered_list[position - 1] is not None:
                instructions = display.color_text("Please choose a blank position.", 'red')
                display.clear_lines(2)
                continue
            
            # Return the valid position
            return position
        
        except ValueError:
            # Handle the case where the input is not a number
            instructions = display.color_text(f"Choose a number between 1 and {config.settings['list_length']}.", 'red')
            display.clear_lines(2)

def update_list(random_number, position):
    numbered_list[position - 1] = random_number

def check_list():
    current_values = [num for num in numbered_list if num is not None]
    if current_values != sorted(current_values):
        return False
    return True

def check_win():
    if None not in numbered_list and check_list():
        return True
    return False

def main():
    while True:
        reset_game()

        while True:
            display.clear()
            display.logo()
            # print(f"Place {config.settings['list_length']} numbers from 1 to {config.settings['random_number_upper_limit']} in order!\n")
            
            print_list()
            random_number = generate_random_number()
            position = collect_position()

            if position == 'q':
                return  # Exit the game completely

            update_list(random_number, position)

            if not check_list():
                display.clear()
                display.logo()
                print_list()
                instructions = display.color_text("Game over.", 'red')
                print(instructions)
                print("[1] Play Again")
                print("[0] Main Menu")
                choice = input("> ").strip()

                while choice not in ['0', '1']:
                    display.clear_lines(3)  # Clear invalid choice message and instructions
                    instructions = display.color_text("Invalid choice. Please select [1] to Play Again or [0] to return to Main Menu.", 'red')
                    print(instructions)
                    print("[1] Play Again")
                    print("[0] Main Menu")
                    choice = input("> ").strip()
                
                if choice == '1':
                    break  # Break the inner loop and start a new game
                elif choice == '0':
                    return  # Exit the game completely

            elif check_win():
                display.clear()
                display.logo()
                print_list()
                instructions = display.color_text("Congratulations! You won!", 'green')
                print(instructions)
                print("[1] Play Again")
                print("[0] Main Menu")
                choice = input("> ").strip()

                while choice not in ['0', '1']:
                    display.clear_lines(3)  # Clear invalid choice message and instructions
                    instructions = display.color_text("Invalid choice. Please select [1] to Play Again or [0] to return to Main Menu.", 'red')
                    print(instructions)
                    print("[1] Play Again")
                    print("[0] Main Menu")
                    choice = input("> ").strip()
                
                if choice == '1':
                    break  # Break the inner loop and start a new game
                elif choice == '0':
                    return  # Exit the game completely

if __name__ == "__main__":
    main()
