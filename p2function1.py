# Ben Pratt

# Function 1: Display an introduction to the game 
# explaining rules and prompt for their name and display 
# that in the welcome message. 
# Return the name to the main program and store it in variable 
# so it can be used throughout the program.


def introduction(): 
    print(f'-' * 40)
    print(f'    Welcome to the BYU Soccer Simulation!')
    print(f'-' * 40)
    print('GAME RULES: ')
    print('' \
    '- Select your home team' \
    '- Your team will randomly face opponents' \
    '- Scores are randomly generated' \
    '- Win 75 percent of games -> NCAA Tournament!' \
    '- Below 50 percent -> Back to practice! ')

    sPlayerName = input("What is your name?: ")
    print(f"Welcome, {sName}! Let's play!")
    return sPlayerName

