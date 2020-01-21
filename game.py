import random

# Creating make_move function
def o_making_move(k):
    if "a" in k:
        grid[0][k] = "o"
    if "b" in k:
        grid[1][k] = "o"
    if "c" in k:
        grid[2][k] = "o"

def x_making_move(k):
    if "a" in k:
        grid[0][k] = "x"
    if "b" in k:
        grid[1][k] = "x"
    if "c" in k:
        grid[2][k] = "x" 

currentplayer = random.choice(["o", "x"])

# Creating grid
grid = [
{"a1" : "_", "a2" : "_", "a3" : "_"}, 
{"b1" : "_", "b2" : "_", "b3" : "_"}, 
{"c1" : "_", "c2" : "_", "c3" : "_"}
]

printable_grid = [
    grid[0].values(), 
    grid[1].values(),
    grid[2].values()
]

for x in printable_grid:
    print(x)

# Yay
# Starting Game
def taketurn(who):
    if who == "o":
        input_o = input("Player o, please type the coordinate of where you'd like to place your symbol. lines = a, b, c; rows = 1, 2, 3.")
        o_making_move(input_o)
        
    if who == "x":
        input_x = input("Player x, please type the coordinate of where you'd like to place your symbol. lines = a, b, c; rows = 1, 2, 3.")
        x_making_move(input_x)
        

won = False

while not won:    
    taketurn(currentplayer)
    if currentplayer == "o":
        currentplayer = "x"
    else:
        currentplayer = "o"
    
    for x in printable_grid:
        print(x)
    

# Creating judge function