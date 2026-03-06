# Riley Hong, Sadie Barton, and Ben Pratt
# P2 soccer program functions

# Display of menu and return choice. 
# Store in variable and use this value to determine which function to call next.

import random

# 2. Display of menu and return choice. Store in variable and use this value to determine which function to call next.
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
bRunning = True
while bRunning == True :
    iChoice = show_menu()
    if iChoice == 1 :
        print("Game Rules")

    elif iChoice == 2 :
        sHomeTeam = list_teams(lstTeams, "\nPick your home team (1-3): ")
        lstTeams.remove(sHomeTeam)
        sOpponent = list_teams(lstTeams, "\nPick your opposing team (1-2): ")
        print(f"\nHome team: {sHomeTeam}")
        print(f"Opponent: {sOpponent}")

        iHomeWins = 0
        iAwayWins = 0

        # THE LISTS:
        lstWonAgainst = []
        lstLostAgainst = [] 
            
        play_game(sOpponent, sHomeTeam)

        if play_game(sOpponent, sHomeTeam) == "W" :
            iHomeWins = iHomeWins + 1
            lstWonAgainst.append(sOpponent)
        else :
            iAwayWins = iAwayWins + 1
            lstLostAgainst.append(sOpponent)

        display_record(sHomeTeam, iHomeWins, iAwayWins, lstWonAgainst, lstLostAgainst)
        

    else :
        print("Quitting game.")
        bRunning = False












