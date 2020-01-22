# Creating Grid
grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

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

draw_line(grid)

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

def o_making_move(k):
    if "a" in k:
        if grid[0][int(k[1])-1] == " ":
            grid[0][int(k[1])-1] = "o"
        else:
            os_move = " "
            print("Oops! Try again.")
            o_making_move(os_move)
    if "b" in k:
        if grid[1][int(k[1])-1] == " ":
            grid[1][int(k[1])-1] = "o"
        else:
            os_move = " "
            print("Oops! Try again.")
            o_making_move(os_move)
    if "c" in k:
        if grid[2][int(k[1])-1] == " ":
            grid[2][int(k[1])-1] = "o"
        else:
            os_move = " "
            print("Oops! Try again.")
            o_making_move(os_move)

def x_making_move(k):
    if "a" in k:
        if grid[0][int(k[1])-1] == " ":
            grid[0][int(k[1])-1] = "x"
        else:
            xs_move = " "
            print("Oops! Try again.")
            o_making_move(xs_move)
    if "b" in k:
        if grid[1][int(k[1])-1] == " ":
            grid[1][int(k[1])-1] = "x"
        else:
            xs_move = " "
            print("Oops! Try again.")
            o_making_move(xs_move)
    if "c" in k:
        if grid[2][int(k[1])-1] == " ":
            grid[2][int(k[1])-1] = "x"
        else:
            xs_move = " "
            print("Oops! Try again.")
            o_making_move(xs_move)


while True:
    os_move = input("o's turn: ")
    o_making_move(os_move)

    draw_line(grid)

    if grid[0][0] == grid[0][1] == grid[0][2] == "o" or grid[1][0] == grid[1][1] == grid[1][2] == "o" or grid[2][0] == grid[2][1] == grid[2][2] == "o" or grid[0][0] == grid[1][0] == grid[2][0] == "o" or grid[0][1] == grid[1][1] == grid[2][1] == "o" or grid[0][2] == grid[1][2] == grid[2][2] == "o" or grid[0][0] == grid[1][1] == grid[2][2] == "o" or grid[0][2] == grid[1][1] == grid[2][0] == "o":
        print("o has won!")
        break

    xs_move = input("x's turn: ")
    x_making_move(xs_move)

    draw_line(grid)

    if grid[0][0] == grid[0][1] == grid[0][2] == "x" or grid[1][0] == grid[1][1] == grid[1][2] == "x" or grid[2][0] == grid[2][1] == grid[2][2] == "x" or grid[0][0] == grid[1][0] == grid[2][0] == "x" or grid[0][1] == grid[1][1] == grid[2][1] == "x" or grid[0][2] == grid[1][2] == grid[2][2] == "x" or grid[0][0] == grid[1][1] == grid[2][2] == "x" or grid[0][2] == grid[1][1] == grid[2][0] == "x":
        print("x has won!")
        break
