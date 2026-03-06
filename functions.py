# Sadie Barton 

# Display an introduction to the game explaining rules and prompt for their name and display that in the welcome message. 
# Return the name to the main program and store it in variable so it can be used throughout the program

# Display list of all teams and allow the user to choose a team using a menu.
# Call the function again to let the user choose the opponent but do not display 
# the team they chose previously. Remove that team from the list. Allow the user to select an opponent, 
# and return team name. This function should receive a parameter but give it a default value if none is passed.
# You can use this function for both choosing the home team and the opponent team.


def sWelcome():
    print("Welcome to the Soccer Game Simulator!")
    print("Rules: ")
    print("1. Each player picks a home team and an opposing team")
    print("2. Teams play against each other and random scores are generated")
    print("3. The team with the higher score wins")
    print("4. There are no ties — a winner is always determined")
    print("5. You can play multiple games from the menu")
    print("6. Your win/loss record is tracked throughout the game")

    sName = input("Enter your name: ").capitalize()
    return sName

sName = sWelcome()
print(f"Welcome {sName}! Let's play!")


lstTeams = ["Cougars", "Utes", "Aggies", "Wildcats", "Bulldogs", "Falcons", "Eagles", "Wolves", "Lions", "Bears"]

def list_teams(lstTeams=[], sPrompt="Make your selection: "):
    print("-- list of Teams --")
    index = 0
    for teams in lstTeams:
        print(f"{index + 1}. {teams}")
        index += 1

    sTeam = int(input(sPrompt))
    return lstTeams[sTeam - 1]

sHomeTeam = list_teams(lstTeams, "Pick your home team (1-3): ")
lstTeams.remove(sHomeTeam)
sOpponent = list_teams(lstTeams, "Pick your opposing team (1-2): ")

print(f"Home team: {sHomeTeam}")
print(f"Opponent: {sOpponent}")
