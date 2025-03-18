# # # # # # # # # # # # # # # # # # # # # # # #
#        Project: ViCalc(Virtual Calculator)  #
#         Author: dreyyan                     #
#       Language: Python                      #
#   Date Started: 03/15/2025                  #
#  Date Finished: 03/16/2025                  #
# # # # # # # # # # # # # # # # # # # # # # # #

''' IMPORTS '''
import os, time, msvcrt

''' FUNCTIONS: UTILITY '''
# FUNCTION: Clear the console screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# FUNCTION: Display formatted lines
def display_format(length):
    for _ in range(1, length + 1):
        print('-', end='')
    print() # Print newline

# FUNCTION: Display character /w delay to mimic animation
def delay(string_input):
    for c in string_input:
        print(c, end='')
        time.sleep(0.005)

# FUNCTION: Display error message format
def error_message(message):
    print(f"ERROR: {message}.")
    time.sleep(2)

''' FUNCTIONS: MAIN '''

# FUNCTION: Display a virtual calculator
def display_calculator(expression):
    # Rows 1-3
    display_format(19)
    print(expression)
    display_format(19)

    # Row 4
    print("  ".join(['|', '1', '|', '2', '|', '3', '|']))
    for _ in range(1, 20):
        print('-', end='')
    print(f"    Space => [+-*/]")

    # Row 5
    print("  ".join(['|', '4', '|', '5', '|', '6', '|']), end='')
    print(f"    Enter => [ = ]")

    # Row 6
    for _ in range(1, 20):
        print('-', end='')
    print(f"    '`'   => [Exit]")

    # Row 7
    print("  ".join(['|', '7', '|', '8', '|', '9', '|']))

    # Row 8
    display_format(19)

# FUNCTION: Display the main menu for the calculator program
def calculator_menu():
    while True:
        clear_screen()
        # Display options
        print("° CALCULATOR °")
        display_format(14)
        print("   1. Start")
        print("   2. Exit")
        display_format(14)

        # Prompt user to enter operation to calculate, gets only one character at a time
        operation_to_perform = msvcrt.getch().decode()

        if not operation_to_perform.isdigit(): # ERROR: Non-integer input
            error_message("Invalid input, please enter a valid integer as choice")

        # Start operations according to choices
        if operation_to_perform == '1':
            start_calculator()
        else:
            print("exiting calculator...", end='')
            time.sleep(1)
            exit(0)

# FUNCTION: Start the main virtual calculator interface
def start_calculator():
    global mathematical_expression  # To store the entire mathematical expression
    mathematical_expression = ""
    current_input = ""  # To store the current value
    input_to_display = "" # To store the expression to display in the calculator
    value_input = 0 # To store each character pressed by the user

    while True:
        clear_screen()
        display_calculator(input_to_display) # Display/update calculator
        value_input = msvcrt.getch().decode() # Get input from the user

        if value_input.isdigit(): # If input is a digit
            current_input += str(value_input) # Add digit to the number
            input_to_display += str(value_input) # Add digit to the displayable input

        elif value_input in ['+', '-', '*', '/']:  # If spacebar is pressed
            current_input += value_input # Add operation sign for display
            input_to_display += value_input # Add operation sign to the displayable input

        elif value_input == '\x08': # If backspace is pressed
            if current_input:  # Check if there is an input to delete
                current_input = current_input[:-1] # Remove last character
                input_to_display = input_to_display[:-1] # Also remove the last character for the display

        elif value_input == '\r': # If enter key is pressed
            # Check if current_input is non-empty and ends with an operator
            if current_input and current_input[-1] in ['+', '-', '*', '/']: # Ends with an operator
                error_message("Invalid input: expression cannot end with an operator.")
                continue

            if current_input:  # Check if current input is not empty
                if mathematical_expression:  # If there's a current mathematical expression
                    mathematical_expression += current_input # Append to the existing expression
                else:
                    mathematical_expression = current_input # Set the expression to the current input
                try:
                    result = eval(mathematical_expression) # Solve the equation

                    # If result is a float and represents a whole number, convert it to an integer
                    if isinstance(result, float) and result.is_integer():
                        result = int(result)

                    input_to_display = str(result) # Display the result
                    mathematical_expression = str(result) # Update expression to the result
                    current_input = ""  # Clear the current input for the next calculation

                except SyntaxError: # EXCEPT: Syntax error if expression is incomplete
                    error_message("Syntax error: Please enter a valid mathematical expression.")
                    continue
                except Exception as e: # EXCEPT: Other errors
                    error_message(f"Error in calculation: {e}")
                    continue
            else:
                error_message("Input cannot be empty. Please enter a valid expression.")
                continue
        elif value_input == '`': # If backtick is pressed
            break # Exit the virtual calculator interface
        else: # Type mismatch
            print("\nInvalid input! Please enter a digit (0-9).")
            time.sleep(2)

    calculator_menu() # Return to main menu

calculator_menu() # Start program
