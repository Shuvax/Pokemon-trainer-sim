import random
# move trainer function
def move_trainer(position,bounds,prob):
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'] 
    choice  = random.choice(directions)
    
    M,N = bounds
    
   
   # print('Direction '+str(choice)+', value {:.2f}'.format(value))
    y,x = position
    
    # all the choices for directions and nested if statements
    if(choice == "E"):
        x += 1
        if(x > N-1):
            x = N-1
    
    if(choice == "NE"):
        x += 1
        y -= 1
        if(x > N-1):
            x = N-1
        if(y < 0):
            y = 0
    
    if(choice == "N"):
        y -= 1
        if(y < 0):
            y = 0
            
    if(choice == "NW"):
        x -= 1
        y -= 1
        if(x < 0):
            x = 0
        if(y < 0):
            y = 0
            
    if(choice == "W"):
        x -= 1
        if(x < 0):
            x = 0
            
    if(choice == "SW"):
        x -= 1
        y += 1
        if(y > M-1):
            y = M-1
        if(x < 0):
            x = 0
                
    if(choice == "S"):
        y += 1
        if(y > M-1):
            y = M-1
    
    if(choice == "SE"):
        x += 1
        y += 1
        if(x > N-1):
            x = N-1
        if(y > M-1):
            y = M-1   
    
    position = y,x
    
    # same code from part 2
    value = random.random()
     
    if value<prob:
        
        return position,True
    else:
       
        return position,False
# run_one_simulation function that was told to be used
# changes the parameters to count for the position and bounds as well
def run_one_simulation( grid, prob, position, bounds ):
    total= 0
    # this is so that the starting position is counted as well for each simulation
    m,n = position
    grid[m][n] += 1
    # for loop for each turn
    for i in range(1,251):
        
        position,caught = move_trainer(position,bounds,p)
        
        if caught == True:
            total+=1
        # no current total is needed for this part
        # two new variables, row and col, that is used in the grid list as indices
        # to add one every time trainer is on the specific position
        row,col = position
        grid[row][col] += 1
    # function returns the total number of caught pokemon for the single simulation   
    return total 
    
# main body 
if __name__ == "__main__":
    
    # all inputs from last part but includes number of runs as a input as well
    M = int(input('Enter the integer number of rows => '))
    print(M)
    N = int(input('Enter the integer number of cols => '))
    print(N)
    p = float(input('Enter the probability of finding a pokemon (<= 1.0) => '))
    print(p)
    runs = int(input('Enter the number of simulations to run => '))
    print(runs)
    print('')
    
    #seed value is given and position is given
    seed_value = 10*M+N
    position = (M//2,N//2)
    bounds = (M,N)
    random.seed(seed_value)
    
    #starting value for the number of pokemon caught at a certain turn
    caught_turn = 0 
    # total pokemon for every turn for every simulation
    tot = 0
    # creates a new list to be used in the following for loop to make a starting 
    # grid depending on M and N
    count_grid = []
    for i in range(M):
        count_grid.append( [0]*N ) 
  
    # creates new list for pokemon caught for each run
    pokemon_caught = []
    
    for i in range(runs):
        # creates a new variable for the return value for total for 
        # run_one_simulation 
        caught_turn = run_one_simulation( count_grid, p, position,bounds )
        # adds to the pokemon_caught list and each index will be the specific turn
        pokemon_caught.append(caught_turn)
        # total pokemon caught for all simulations ran
        tot += caught_turn

    # variables for the maximum and minimum number of pokemon caught from all the
    # runs. Also finds the index which is the specific number simulation
    max_caught = max(pokemon_caught) 
    index_max_caught = pokemon_caught.index(max_caught)
    min_caught = min(pokemon_caught) 
    index_min_caught = pokemon_caught.index(min_caught)
    
    # new list variable for the upcoming flattened list
    oneDgrid = []
    
    # nested for loops to create the new grid
    for j in count_grid:
        for i in j:
            print ('{:5d}'.format(i),end='')
            
        print('') 
        # joins all the lists in the grid together to make a flattened list
        oneDgrid += j
    # variables for the minimum and maximum of the flattened list to find 
    # minimum and maximum values over all simulations
    min_visited = min(oneDgrid)
    max_visited = max(oneDgrid)
    
    # print statements that are formatted for the wanted output
    print('\nTotal pokemon caught is ',tot,sep='')
    print('Minimum pokemon caught was ',min_caught,' in simulation ',index_min_caught+1,sep='')
    print('Maximum pokemon caught was ',max_caught,' in simulation ',index_max_caught+1,sep='')
    print('The least visited space was visited ',min_visited,' times',sep='')
    print('The most visited space was visited ',max_visited,' times',sep='')
   