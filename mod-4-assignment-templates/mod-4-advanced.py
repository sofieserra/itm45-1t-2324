'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def relationship_status(from_member, to_member, social_graph):
    if from_member in social_graph and to_member in social_graph:
        if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
            return str("friends")
        elif to_member in social_graph[from_member]["following"]:
            return str("follower")
        elif from_member in social_graph[to_member]["following"]:
            return str("followed by")

    return str("no relationship")

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "Following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

def get_user_details(username, social_graph):
    if username in social_graph:
        user_details = social_graph[username]
        return user_details["first_name"], user_details["last_name"]
    else:
        return None, None

from_member_username = str(input("Enter the first member's username:"))
from_first_name, from_last_name = get_user_details(from_member_username, social_graph)

to_member_username = str(input("Enter the second member's username:"))
to_first_name, to_last_name = get_user_details(to_member_username, social_graph)

relationship = relationship_status(from_member_username, to_member_username, social_graph)

if from_first_name and from_last_name and to_first_name and to_last_name:
    print("The relationship between", from_first_name, from_last_name, "and", to_first_name, to_last_name, "is:", relationship)
else:
    print("One or more members not found.")

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may be 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def tic_tac_toe(board):
    winner = check_rows(board)
    if not winner:
        winner = check_columns(board)
    if not winner:
        winner = check_diagonals(board)
    return str(winner) if winner is not None else "NO WINNER"

def check_rows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return None

def check_columns(board):
    for col in range(len(board)):
        column_values = [board[row][col] for row in range(len(board))]
        if len(set(column_values)) == 1:
            return column_values[0]
    return None

def check_diagonals(board):
    diagonal1 = [board[i][i] for i in range(len(board))]
    diagonal2 = [board[i][len(board) - 1 - i] for i in range(len(board))]
    if len(set(diagonal1)) == 1:
        return diagonal1[0]
    elif len(set(diagonal2)) == 1:
        return diagonal2[0]
    return None
board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

boards = [board1, board2, board3, board4, board5, board6, board7]

for idx, board in enumerate(boards, start=1):
    result = tic_tac_toe(board)
    print(f"Board {idx}: Winner - {result}")

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def eta(first_stop, second_stop, route_map):
        current_stop = first_stop
        total_time = 0
        found_route = False
        
        while current_stop != second_stop:
            leg = (current_stop, second_stop)
            if leg in route_map:
                total_time += route_map[leg]['travel_time_mins']
                found_route = True
                break
    
            leg_found = False
            for leg_key in route_map:
                if leg_key[0] == current_stop:
                    next_stop = leg_key[1]
                    total_time += route_map[leg_key]['travel_time_mins']
                    current_stop = next_stop
                    leg_found = True
                    break
    
                if not leg_found:
                    return "Route not found between stops"
    
        if found_route:
            return total

legs1 = {
     ('up,'admin):{
         'travel_time_mins': 10
     },
     ('admin,'dlsu'):{
         'travel_time_mins': 35
     },
     ('dlsu','upd'):{
         'travel_time_mins': 55
     }
}

legs2 = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}

first_stop_input = input("Enter the starting stop:")
second_stop_input = input("Enter the destination stop:")

result1 = eta(first_stop_input, second_stop_input, legs1)
result2 = eta(first_stop_input, second_stop_input, legs2)

if isinstance(result1, int):
    print(f"ETA from {first_stop_input} to {second_stop_input}: {result1} minutes")
else:
    print(result1)
    
if isinstance(result2, int):
    print(f"ETA from {first_stop_input} to {second_stop_input}: {result1} minutes")
elif result2 != "Route not found between stops":
    print(result2)
