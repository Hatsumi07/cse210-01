#week02 prove: Tic-Tac-Toe game by Crystal Cardenas
grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
def x_turn():
    cell_number = int(input("x's turn to choose a square (1-9):"))
    if 0 < cell_number < 10:
        if check_ocupied(cell_number) == True:
            print("\033[31m This square is ocupied!\033[0m")
            x_turn()
        else:
            grid_draws(cell_number, "\033[32m X\033[37m")
            display_grid()
    else:
        x_turn()

def o_turn():
    cell_number = int(input("o's turn to choose a square (1-9):"))
    if 0 < cell_number < 10:
        if check_ocupied(cell_number) == True:
            print("\033[31m This square is ocupied!\033[0m")
            o_turn()
        else:
            grid_draws(cell_number, "\033[35m O\033[37m")
            display_grid()
    else:
        o_turn()

def display_grid():

    print(" " + grid[0] + " | " + grid[1] + " | " + grid[2] + " ")
    print(" - + - + -")
    print(" " + grid[3] + " | " + grid[4] + " | " + grid[5] + " ")
    print(" - + - + -")
    print(" " + grid[6] + " | " + grid[7] + " | " + grid[8] + " ")
    print()

def check_ocupied(cell_number):  
    index = cell_number - 1
    if (grid[index] == str(cell_number)):
        return False
    else:
        return True   

def grid_draws(input, marker):
    if input == 1:
        grid[0] = marker
    elif input == 2:
        grid[1] = marker 
    elif input == 3:
        grid[2] = marker
    elif input == 4:
        grid[3] = marker
    elif input == 5:
        grid[4] = marker
    elif input == 6:
        grid[5] = marker 
    elif input == 7:
        grid[6] = marker
    elif input == 8:
        grid[7] = marker
    elif input == 9:
        grid[8] = marker                                         

def win1():
    if ((grid[0] == grid[1]) and (grid[1] == grid[2])):
        return True
def win2():
    if ((grid[3] == grid[4]) and (grid[4] == grid[5])):
        return True
def win3():
    if ((grid[6] == grid[7]) and (grid[7] == grid[8])):
        return True
def win4():
    if ((grid[0] == grid[3]) and (grid[3] == grid[6])):
        return True
def win5():
    if ((grid[1] == grid[4]) and (grid[4] == grid[7])):
        return True
def win6():
    if ((grid[2] == grid[5]) and (grid[5] == grid[8])):
        return True
def win7():
    if ((grid[0] == grid[4]) and (grid[4] == grid[8])):
        return True
def win8():
    if ((grid[2] == grid[4]) and (grid[4] == grid[6])):
        return True
def check_win(marker):
    x_color = "\033[0;30;42m"
    o_color = "\033[0;30;45m"
    if (win1() or win2() or  win3() or win4() or win5() or win6() or win7() or win8()):
        if win1() == True:
            if marker == "X":
                display_winner_grid(1, marker, x_color)
            elif marker == "O":
                display_winner_grid(1, marker, o_color)   
        elif win2() == True:
            if marker == "X":
                display_winner_grid(2, marker, x_color)
            elif marker == "O":
                display_winner_grid(2, marker, o_color)
        elif win3() == True:
            if marker == "X":
                display_winner_grid(3, marker, x_color)
            elif marker == "O":
                display_winner_grid(3, marker, o_color)
        elif win4() == True:
            if marker == "X":
                display_winner_grid(4, marker, x_color)
            elif marker == "O":
                display_winner_grid(4, marker, o_color)
        elif win5() == True:
            if marker == "X":
                display_winner_grid(5, marker, x_color)
            elif marker == "O":
                display_winner_grid(5, marker, o_color)
        elif win6() == True:
            if marker == "X":
                display_winner_grid(6, marker, x_color)
            elif marker == "O":
                display_winner_grid(6, marker, o_color)
        elif win7() == True:
            if marker == "X":
                display_winner_grid(7, marker, x_color)
            elif marker == "O":
                display_winner_grid(7, marker, o_color)
        elif win8() == True:
            if marker == "X":
                display_winner_grid(8, marker, x_color)
            elif marker == "O":
                display_winner_grid(8, marker, o_color)   
        return True
    return False    
def display_winner_grid(row, marker, color_start):
    if row == 1:
        grid[0] = color_start + marker + "\033[0m"
        grid[1] = color_start + marker + "\033[0m"
        grid[2] = color_start + marker + "\033[0m"
    elif row == 2:
        grid[3] = color_start + marker + "\033[0m"
        grid[4] = color_start + marker + "\033[0m"
        grid[5] = color_start + marker + "\033[0m"
    elif row == 3:
        grid[6] = color_start + marker + "\033[0m"
        grid[7] = color_start + marker + "\033[0m"
        grid[8] = color_start + marker + "\033[0m"
    elif row == 4:
        grid[0] = color_start + marker + "\033[0m"
        grid[3] = color_start + marker + "\033[0m"
        grid[6] = color_start + marker + "\033[0m"
    elif row == 5:
        grid[1] = color_start + marker + "\033[0m"
        grid[4] = color_start + marker + "\033[0m"
        grid[7] = color_start + marker + "\033[0m"
    elif row == 6:
        grid[2] = color_start + marker + "\033[0m"
        grid[5] = color_start + marker + "\033[0m"
        grid[8] = color_start + marker + "\033[0m"
    elif row == 7:
        grid[0] = color_start + marker + "\033[0m"
        grid[4] = color_start + marker + "\033[0m"
        grid[8] = color_start + marker + "\033[0m"
    elif row == 8:
        grid[2] = color_start + marker + "\033[0m"
        grid[4] = color_start + marker + "\033[0m"
        grid[6] = color_start + marker + "\033[0m"

def main():
    display_grid()
    while (check_win("") == False):
        x_turn()
        check_win("X")
        if check_win("X") == True:
            break
        o_turn()
        check_win("O")
    display_grid()    
    print("Good game. Thanks for playing!")    

main()