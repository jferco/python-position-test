from randomTeamAssign import validate_amounts, print_Result
import re



regex=r'[a-z A-Z 0-9]*'

def menu_control():
    print ("\n-----------Welcome to the random team assign system")

    print("Please enter each team's name and hit enter.")

    print("Once you're done, please type DONE (all caps) and hit enter")
    teams = []
    people = []
    team_input=True
    while(team_input):
        temp_team = input("Enter team name: ")
        if temp_team=="DONE":
            team_input= False
            break
        is_valid  = re.search(regex,temp_team)
        if is_valid.span()[1] == 0:
            print ("Invalid name!. Please try again")
        else:
            teams.append(temp_team)

    print("All teams set!")
    print("Please enter each person's name and hit enter.")

    print("Once you're done, please type DONE (all caps) and hit enter")

    people_input=True
    while(people_input):
        temp_people = input("Enter Person name: ")
        if temp_people=="DONE":
            people_input= False
            break
        is_valid  = re.search(regex,temp_people)
        if is_valid.span()[1] == 0:
            print ("Invalid name!. Please try again")
        else:
            people.append(temp_people)


    if validate_amounts(teams,people):
        print("\n \n --- HERE ARE YOUR TEAMS --- \n \n")
        print_Result(teams,people)
        ending_control("\n-----------------------\n")
    else:
        ending_control("ERROR! \n You need at least 2 teams and 2 people per team!!")


def ending_control(message):
    print (message)

    play_again = input("If you wish to continue type 'y'. If not, type anything else:  ")

    play_again=play_again.lower()

    if play_again == 'y':
        menu_control()
    else:
        return None

menu_control()