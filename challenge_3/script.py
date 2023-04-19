def decode_password(instructions):
    keypad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    current_button = '5'  # Setting the starting btn to 5
    password = ""  # Passwrd

    for line in instructions:
        for move in line:
            # Update current button based on moves
            if move == 'U':
                if current_button not in ['1', '2', '3']:
                    current_button = str(int(current_button) - 3)
            elif move == 'D':
                if current_button not in ['7', '8', '9']:
                    current_button = str(int(current_button) + 3)
            elif move == 'L':
                if current_button not in ['1', '4', '7']:
                    current_button = str(int(current_button) - 1)
            elif move == 'R':
                if current_button not in ['3', '6', '9']:
                    current_button = str(int(current_button) + 1)

        password += current_button  # Add current button to password

    return password


# Read instructions from doc
with open('t.txt', 'r') as file:
    instructions = file.read().splitlines()

# Decode password from instructions
password = decode_password(instructions)
# Printing the password
print(password)