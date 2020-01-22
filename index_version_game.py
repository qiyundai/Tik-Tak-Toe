# Creating Grid
grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

dic = {'a' : 0, "b" : 1, "c" : 2}
winnerannouncement = "Congratulations to player x!"
os_move = ""
xs_move = ""
won = False

def draw_line(g):
    printable = [
        ["  1   2   3  "],
        ["a ", g[0][0]," | ", g[0][1]," | ", g[0][2]],
        [" --- --- ---"],
        ["b ", g[1][0]," | ", g[1][1]," | ", g[1][2]],
        [" --- --- ---"],
        ["c ", g[2][0]," | ", g[2][1]," | ", g[2][2]]
    ]
    for i in printable:
        print(*i, sep="")

def if_valid(om):
    return grid[dic[om[0]]][int(om[1])-1] == " "

#printable_grid = [
#    [" ", grid[0][0]," | ", grid[0][1]," | ", grid[0][2]],
#    ["--- --- ---"],
#    [" ", grid[1][0]," | ", grid[1][1]," | ", grid[1][2]],
#    ["--- --- ---"],
#    [" ", grid[2][0]," | ", grid[2][1]," | ", grid[2][2]]
#]

#for i in printable_grid:
#    print(*i, sep="")

#Creating game mechanism:
def o_win(r,c):
    return grid[r][c] == grid[r][c+1] == grid[r][c+2] == "o" or grid[r][c] == grid[r+1][c] == grid[r+2][c] == "o" or grid[r][c] == grid[r+1][c+1] == grid[r+2][c+2] == "o" or grid[r][c+2] == grid[r+1][c+1] == grid[r+2][c] == "o"
    
    
def x_win(r,c):
    return grid[r][c] == grid[r][c+1] == grid[r][c+2] == "x" or grid[r][c] == grid[r+1][c] == grid[r+2][c] == "x" or grid[r][c] == grid[r+1][c+1] == grid[r+2][c+2] == "x" or grid[r][c+2] == grid[r+1][c+1] == grid[r+2][c] == "x"

def o_making_move(k):
    k = input("o's turn: ")
    while not if_valid(k):
        k = input("Oops!")  
    grid[dic[k[0]]][int(k[1])-1] = "o"
    draw_line(grid)

def x_making_move(k):
    k = input("x's turn: ")
    while not if_valid(k):
        k = input("Oops!")
    grid[dic[k[0]]][int(k[1])-1] = "x"
    draw_line(grid)
    


#o_won = grid[0][0] == grid[0][1] == grid[0][2] == "o" or grid[1][0] == grid[1][1] == grid[1][2] == "o" or grid[2][0] == grid[2][1] == grid[2][2] == "o" or grid[0][0] == grid[1][0] == grid[2][0] == "o" or grid[0][1] == grid[1][1] == grid[2][1] == "o" or grid[0][2] == grid[1][2] == grid[2][2] == "o" or grid[0][0] == grid[1][1] == grid[2][2] == "o" or grid[0][2] == grid[1][1] == grid[2][0] == "o"

draw_line(grid)

while not won:
    o_making_move(os_move)
    won = o_win(0,0)
    if won:
        break
    x_making_move(xs_move)
    won = x_win(0,0)

print(winnerannouncement)

#if grid[0][0] == grid[0][1] == grid[0][2] == "x" or grid[1][0] == grid[1][1] == grid[1][2] == "x" or grid[2][0] == grid[2][1] == grid[2][2] == "x" or grid[0][0] == grid[1][0] == grid[2][0] == "x" or grid[0][1] == grid[1][1] == grid[2][1] == "x" or grid[0][2] == grid[1][2] == grid[2][2] == "x" or grid[0][0] == grid[1][1] == grid[2][2] == "x" or grid[0][2] == grid[1][1] == grid[2][0] == "x":
#        print("x has won!")
