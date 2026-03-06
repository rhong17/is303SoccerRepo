# Sadie Barton 

# Display list of all teams and allow the user to choose a team using a menu.
# Call the function again to let the user choose the opponent but do not display 
# the team they chose previously. Remove that team from the list. Allow the user to select an opponent, 
# and return team name. This function should receive a parameter but give it a default value if none is passed.
# You can use this function for both choosing the home team and the opponent team.

lstTeams = ["Cougars", "Utes", "Aggies"]

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
