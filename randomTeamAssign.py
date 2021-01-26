# imports python random library
import random

# returns a random element from a list 
def get_random_choice(pList):
    return random.choice(pList)


# Builds an empty matrix to distribute teams
def build_teams_matrix(teams):
    matrix =[]
    for i in range(len(teams)):
        matrix.append([teams[i],[]])
    return matrix

# Fills a team matrix with random distribution
def fill_teams(teams, people):


    teamMatrix = build_teams_matrix(teams)
    random.shuffle(people)
    teams_last_index = len(teamMatrix) -1
    teams_index = 0
    for person in people:
        teamMatrix[teams_index][1].append(person)
        teams_index += 1
        if teams_index > teams_last_index:
            teams_index = 0
    return teamMatrix

# Checks if there's enough people to fill at least 2 per team

def validate_amounts(teams, people):
    team_size = len(teams)
    people_size = len(people)

    return team_size >=2 and people_size >= team_size*2

# Checks if every team on the matrix has at least 2 people
def validate_matrix(matrix):
    for team in matrix:
        team_size = len(team[1])
        if team_size<2:
            return False
    return True

# Flattens all the distributed people in one array
# This function was made to avoid the elimination by reference in the people array
def flatten_people(matrix):
    
    flattened_people=[]

    for people in matrix:
        for subpeople in people[1]:
            flattened_people.append(subpeople)
    return flattened_people

# Main function that returns a valid team matrix (valid == at least 2 people per team)
def team_build_control(teams, people):
    matrix1=fill_teams(teams,people)

    is_valid= validate_matrix(matrix1)
    # if the matrix is not valid, the people is merged in one array, then the matrix will be rebuilt until it produces a valid one
    while(not is_valid):
        people= flatten_people(matrix1)
        matrix1= fill_teams(teams,people)
        is_valid= validate_matrix(matrix1)
    return matrix1

# Function that prints the teams matrix to the console
def print_Result(teams, people):
    random_teams = team_build_control(teams,people)
    for team in random_teams:
        line=team[0] + ": "
        for person in team[1]:
            line+= person+", "
        # prints without the last 2 characters to remove the last colon and space
        print(line[:-2])
    
def no_menu_run(teams, people):
    if type(teams) is not list and type(people) is not list:
        print( "Teams and people parameters should be a list")
        return None
    for team in teams:
        if type(team) is not str:
            print( "Teams list should contain only strings")
            return None

    for person in people:
        if type(person) is not str:
            print( "People list should contain only strings")
            return None
    if not validate_amounts(teams,people):
        print( "There should be at least 2 teams and 2 people per team")
        return None
    print_Result(teams, people)


    
    





# If you want to test only the functions without the menu, uncomment the next lines and execute just this file.

no_menu_run(['t1','t2','t3'],['p1','p2','p3','p4','p5','p6','p7'])
#no_menu_run(['t1','tx','ty'],['p1','p2','p3','p4','p5','p6','p7','p8','p9', 'p10'])


