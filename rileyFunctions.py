# Riley Hong
# P2 soccer program functions

# Display of menu and return choice. 
# Store in variable and use this value to determine which function to call next.


# 2. Display of menu and return choice. Store in variable and use this value to determine which function to call next.
def show_menu() : 
    while True :
        print("1 - Game Rules")
        print("2 - Select Team")
        print("3 - Quit Game")

        iChoice = int(input("Make a selection: "))

        if iChoice != 1 and iChoice != 2 and iChoice != 3 :
                print("Enter a valid choice")
        else :
            return iChoice


# 4. Play the game receiving both team names. Generate random scores without ties. Return W or L.
def play_game(homeTeam, awayTeam) :
    iRandScoreHome = random.randrange(0, 4)
    iRandScoreAway = random.randrange(0, 4)

    while (iRandScoreAway == iRandScoreHome) :
        iRandScoreHome = random.randrange(0, 4)
        iRandScoreAway = random.randrange(0, 4)

    if iRandScoreHome > iRandScoreAway :
        sResult = "W"
    else :
        sResult = "L"
    
    return sResult


