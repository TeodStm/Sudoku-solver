
# A Backtracking program  in Python to solve Sudoku problem 
import time

#cell_variables = {}
  
# A Utility Function to print the Grid 
def print_grid(arr): 
    for i in range(9): 
        for j in range(9): 
            print(arr[i][j], end='')
        print ('')
  
def print_grid_table(arr):
    print("-------------------------")
    for i in range(9):
        print("|", end=' ')
        for j in range(3):
            print(arr[i][j], end=' ')
        print('| ', end='')

        for j in range(3, 6):
            print(arr[i][j], end=' ')
        print('| ', end='')

        for j in range(6,9):
            print(arr[i][j], end=' ')
        print('|', end='\n')
        if (i+1) % 3 == 0 and i != 0:
            print("-------------------------")

    #print("------------------")

count = 0
# Function to Find the entry in the Grid that is still  not used 
# Searches the grid to find an entry that is still unassigned. If 
# found, the reference parameters row, col will be set the location 
# that is unassigned, and true is returned. If no unassigned entries 
# remains, false is returned. 
# 'l' is a list  variable that has been passed from the solve_sudoku function 
# to keep track of incrementation of Rows and Columns 
def find_empty_location(arr, l): 
    for row in range(9): 
        for col in range(9): 
            if(arr[row][col]== 0): 
                l[0]= row 
                l[1]= col 
                return True
    return False

def find_next_cell(arr, cell_varables, l):
    if len(cell_variables) == 0:
        return False

    min_values = 10
    key = (0,0)
    for k in cell_variables.keys():
        if len(cell_variables[k]) < min_values:
            min_values = len(cell_variables[k])
            key = k
    l[0] = k[0]
    l[1] = k[1]
    return True

# Returns a boolean which indicates whether any assigned entry 
# in the specified row matches the given number. 
def used_in_row(arr, row, num): 
    for i in range(9): 
        if(arr[row][i] == num): 
            return True
    return False
  
# Returns a boolean which indicates whether any assigned entry 
# in the specified column matches the given number. 
def used_in_col(arr, col, num): 
    for i in range(9): 
        if(arr[i][col] == num): 
            return True
    return False
  
# Returns a boolean which indicates whether any assigned entry 
# within the specified 3x3 box matches the given number 
def used_in_box(arr, row, col, num): 
    for i in range(3): 
        for j in range(3): 
            if(arr[i + row][j + col] == num): 
                return True
    return False
  
# Checks whether it will be legal to assign num to the given row, col 
# Returns a boolean which indicates whether it will be legal to assign 
# num to the given row, col location. 
def check_location_is_safe(arr, row, col, num): 
      
    # Check if 'num' is not already placed in current row, 
    # current column and current 3x3 box 
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3, col - col % 3, num) 
  
# Takes a partially filled-in grid and attempts to assign values to 
# all unassigned locations in such a way to meet the requirements 
# for Sudoku solution (non-duplication across rows, columns, and boxes) 
def solve_sudoku(arr, cell_variables): 
    global count
    # 'l' is a list variable that keeps the record of row and col in find_empty_location Function     
    l =[0, 0] 
      
    # If there is no unassigned location, we are done     
    #if(not find_empty_location(arr, l)): 
    #    return True

    if(not find_next_cell(arr, cell_variables, l)):
        return True
      
    # Assigning list values to row and col that we got from the above Function  
    row = l[0] 
    col = l[1] 

    for num in cell_variables[(row, col)]:
        arr[row][col] = num
        new_cell_variables = cell_variables
        del new_cell_variables[(row, col)]
        propagate_consraint(arr, new_cell_variables)

        if solve_sudoku(arr, new_cell_variables) == True:
            return True

        arr[row][col] = 0
    # consider digits 1 to 9 
    for num in range(1, 10): 
          
        # if looks promising 
        if(check_location_is_safe(arr, row, col, num)): 
              
            # make tentative assignment 
            arr[row][col]= num 
  
            # return, if success, ya ! if(solve_sudoku(arr)):
            if (solve_sudoku(arr)):
                return True
  
            #print(count)
            count += 1
            #print_grid_table(grid)

            # failure, unmake & try again 
            arr[row][col] = 0
              
    # this triggers backtracking         
    return False

def init_constraint_vars(arr):
    cell_variables = {}
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                cell_variables[(i,j)] = [1,2,3,4,5,6,7,8,9]
    return cell_variables

def propagate_consraints(arr, cell_variables):
    #return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3, col - col % 3, num) 
    for k in cell_variables.keys():
        valid_nums = []
        for num in cell_variables.get(k):
            if not used_in_row(arr, k[0], num) and not used_in_col(arr, k[1], num) and not used_in_box(arr, k[0] - k[0] % 3, k[1] - k[1] % 3, num):
                valid_nums.append(num)
        if len(valid_nums) == 0:
            del cell_variables[k]
        else:
            cell_variables[k] = valid_nums  ## update valid numbers for that cell
    
    for i in cell_variables.items():
        print(i[0], "  --  ", i[1])
    return True

        



# Driver main function to test above functions 
if __name__=="__main__": 
      
    # creating a 2D array for the grid 
    grid =[[0 for x in range(9)]for y in range(9)]
    
      
    # assigning values to the grid 
    grid1 =[[3, 0, 6, 5, 0, 8, 4, 0, 0], 
           [5, 2, 0, 0, 0, 0, 0, 0, 0], 
           [0, 8, 7, 0, 0, 0, 0, 3, 1], 
           [0, 0, 3, 0, 1, 0, 0, 8, 0], 
           [9, 0, 0, 8, 6, 3, 0, 0, 5], 
           [0, 5, 0, 0, 9, 0, 6, 0, 0], 
           [1, 3, 0, 0, 0, 0, 2, 5, 0], 
           [0, 0, 0, 0, 0, 0, 0, 7, 4], 
           [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    # hard
    grid = [[0, 0, 0, 0, 0, 0, 6, 8, 0], 
            [0, 0, 0, 0, 7, 3, 0, 0, 9], 
            [3, 0, 9, 0, 0, 0, 0, 4, 5], 
            [4, 9, 0, 0, 0, 0, 0, 0, 0], 
            [8, 0, 3, 0, 5, 0, 9, 0, 2], 
            [0, 0, 0, 0, 0, 0, 0, 3, 6], 
            [9, 6, 0, 0, 0, 0, 3, 0, 8], 
            [7, 0, 0, 6, 8, 0, 0, 0, 0], 
            [0, 2, 8, 0, 0, 0, 0, 0, 0]]
      
    cell_variables = init_constraint_vars(grid)
    propagate_consraints(grid, cell_variables)


    # if success print the grid 
    if(solve_sudoku(grid, cell_variables)): 
        #print_grid(grid)
        print("")
        print_grid_table(grid) 
    else: 
        print("No solution exists")
  
# The above code has been contributed by Harshit Sidhwa. 
