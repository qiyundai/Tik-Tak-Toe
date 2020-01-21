# Creating Grid
grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

printable_grid = [
    [grid[0][0],"  |", grid[0][1],"  |", grid[0][2]],
    ["--- --- ---"],
    [grid[1][0],"  |", grid[1][1],"  |", grid[1][2]],
    ["--- --- ---"],
    [grid[2][0],"  |", grid[2][1],"  |", grid[2][2]]
]

for i in printable_grid:
    print(*i, sep="")

#Creating game mechanism:
won = False

def o_making_move(k):
    if "a" in k:
        grid[0][int(k[1])] == "o"
    if "b" in k:
        grid[1][int(k[1])] == "o"
    if "c" in k:
        grid[2][int(k[1])] == "o"

def x_making_move(k):
    if "a" in k:
        grid[0][int(k[1])] == "x"
    if "b" in k:
        grid[1][int(k[1])] == "x"
    if "c" in k:
        grid[2][int(k[1])] == "x" 

   
while not won:
    os_move = input("o's turn: ")
    o_making_move(os_move)
    for i in printable_grid:
        print(*i, sep="")
    if grid[0][0] == grid[0][1] == grid[0][2] == "o" or grid[1][0] == grid[1][1] == grid[0][2] == "o" or grid[2][0] == grid[2][1] == grid[2][2] == "o" or grid[0][0] == grid[1][0] == grid[1][0] == "o" or grid[0][1] == grid[1][1] == grid[2][1] == "o" or grid[0][2] == grid[1][2] == grid[2][2] == "o" or grid[0][0] == grid[1][1] == grid[2][2] == "o" or grid[0][2] == grid[1][1] == grid[0][2] == "o":
        won = True
        print("o has won!")

    xs_move = input("x's turn: ")
    x_making_move(xs_move)
    for i in printable_grid:
        print(*i, sep="")
    if grid[0][0] == grid[0][1] == grid[0][2] == "x" or grid[1][0] == grid[1][1] == grid[0][2] == "x" or grid[2][0] == grid[2][1] == grid[2][2] == "x" or grid[0][0] == grid[1][0] == grid[1][0] == "x" or grid[0][1] == grid[1][1] == grid[2][1] == "x" or grid[0][2] == grid[1][2] == grid[2][2] == "x" or grid[0][0] == grid[1][1] == grid[2][2] == "x" or grid[0][2] == grid[1][1] == grid[0][2] == "x":
        won = True
        print("x has won!")

