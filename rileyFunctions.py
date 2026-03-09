# Riley Hong, Sadie Barton, and Ben Pratt
# P2 soccer program functions


import random

# 1. Display an introduction to the game 
# Ben Pratt

def introduction(): 
    while True :
        print(f'-' * 40)
        print(f'    Welcome to the BYU Soccer Simulation!')
        print(f'-' * 40)
        print('\nGAME RULES: ')
        print('' \
        '\n- Select your home team' \
        '- Your team will randomly face opponents' \
        '- Scores are randomly generated' \
        '- Win 75 percent of games -> NCAA Tournament!' \
        '- Below 50 percent -> Back to practice! ')

        sPlayerName = input("\nWhat is your name?: ")
        print(f"Welcome, {sPlayerName}! Let's play!")
        return sPlayerName


# 2. Display of menu and return choice. Store in variable and use this value to determine which function to call next.
# Riley Hong
def show_menu() : 
    while True :
        print("\n1 - Game Rules")
        print("2 - Select Team")
        print("3 - Quit Game")

        iChoice = int(input("\nMake a selection: "))

        if iChoice != 1 and iChoice != 2 and iChoice != 3 :
                print("Enter a valid choice")
        else :
            return iChoice
            

# 3. Display list of all teams and allow the user to choose a team using a menu.
# Sadie Barton
lstTeams = ["Cougars", "Utes", "Aggies", "Wildcats", "Bulldogs", "Falcons", "Eagles", "Wolves", "Lions", "Bears"]

def list_teams(lstTeams=[], sPrompt= "Make your selection: "):
    print("\n-- List of Teams --")
    index = 0
    for teams in lstTeams:
        print(f"{index + 1}. {teams}")
        index += 1

    sTeam = int(input(sPrompt))
    return lstTeams[sTeam - 1]


# 4. Play the game receiving both team names. Generate random scores without ties. Return W or L.
# Riley Hong
def play_game(sHomeTeam, sAwayTeam) :
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


# 5. Display the final record for a team. Receive the home team data and display information.
# Riley Hong
def display_record(sHomeTeam, iHomeWins, iAwayWins, lstWonAgainst, lstLostAgainst) :
    print("\nTeams won against: ")
    for team in lstWonAgainst :
        print(team)
    print("Teams lost against: ")
    for team in lstLostAgainst :
        print(team)
    print(f"\nFinal season record: {iHomeWins} - {iAwayWins}")

    fWinPercentage = iHomeWins / (iHomeWins + iAwayWins)

    if fWinPercentage >= 0.75 :
        print("Qualified for the NCAA Soccer Tournament!")
    elif fWinPercentage >= 0.5 :
        print("You had a good season.")
    else : 
        print("Your team needs to practice!")



# THE MAIN PROGRAM: 
# Riley Hong, Ben Pratt, Sadie Barton
sPlayerName = introduction()
lstOpp = []
bRunning = True
while bRunning == True :
    iChoice = show_menu()
    if iChoice == 1 :
        introduction()
    elif iChoice == 2 :
        sHomeTeam = list_teams(lstTeams, "\nPick your home team (enter number 1-10): ")
        lstTeams.remove(sHomeTeam)
        iGames = int(input(f"Enter the number of games that {sHomeTeam} will play this season (enter number between 1-9): "))
        for iGames in range(0, iGames) :
            sOpponent = list_teams(lstTeams, "\nPick your opposing team (enter number): ")
            lstTeams.remove(sOpponent)
            lstOpp.append(sOpponent)
        print(f"\nHome team: {sHomeTeam}")
        print(f"Opponents: {', '.join(lstOpp)}")

        iHomeWins = 0
        iAwayWins = 0

        # THE LISTS:
        lstWonAgainst = []
        lstLostAgainst = [] 
        
        for team in lstOpp :
            sResult = play_game(sHomeTeam, team)

            if sResult == "W" :
                iHomeWins = iHomeWins + 1
                lstWonAgainst.append(team)
            else :
                iAwayWins = iAwayWins + 1
                lstLostAgainst.append(team)

        display_record(sHomeTeam, iHomeWins, iAwayWins, lstWonAgainst, lstLostAgainst)
        bRunning = False
        

    else :
        print("Quitting game.")
        bRunning = False












