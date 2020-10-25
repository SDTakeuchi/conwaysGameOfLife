import random, time, copy
WIDTH = 40
HEIGHT = 9

#Creating a list of list for the cells
nextCells = []
for x in range(WIDTH):
    column = [] #create a new column
    for y in range(HEIGHT):
        if random.randint(0,1)==0:
            column.append('#') #adding a living cell
        else:
            column.append('') #adding a dead cell
    nextCells.append(column)

while True: #main program loop
    print('\n\n\n\n\n')#separate each step with new lines
    currentCells = copy.deepcopy(nextCells)

    #print currentCells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')#print '#' or space
        print()#print a new line at the end of the row

    #calculate the next step's cells based on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT): #get neighboring coordinates
            leftCoord = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y-1) % HEIGHT
            belowCoord = (y+1) % HEIGHT

            #count number of living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1
            
            #set cell besed on Conway's Game of life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3): #originally numNeighbors == 2 or numNeighbors == 3
                #living cells with 2 or 3 neighbors stay alive
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                #dead cells with 3 neighbors come alive
                nextCells[x][y] = '#'
            else:
                #everything else stay alive or dies
                nextCells[x][y] = ' '
    time.sleep(1)

