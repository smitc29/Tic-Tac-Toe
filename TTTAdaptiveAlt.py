import random

grid = [" "," "," "," "," "," "," "," "," "] # Determines appearance/status of grid

winner = False # determines if game ends in tie or not

Brain = [0, 1, 2, 3, 4, 5, 6, 7, 8] # Used to store AI's possible moves

PlayAgain = True # Used to see if user wants to play again

def reset(MyList): # Used to fill list with blank spaces for a new game
    temp = 0
    while temp < len(MyList):
        MyList[temp] = " "
        temp += 1


def wincheck(MyList, A, B, C): # Used to see if a player has won the game yet
    if MyList[A] == MyList[B] == MyList[C]:
        if MyList[A] == "X":
            print("X wins")
            return True
        elif MyList[A] == "O":
            print("O wins")
            return True
    return False

def AICheck(MyList, A, B, C): # Used to see if there's 2 X/Os potentially about to win
    if MyList[A] == MyList[B] and MyList[A] != MyList[C] and MyList[A] != " " and MyList[C] == " ":
        #Spaces A and B are equal, but not A and C; 
        #List[C] is open, List[A] is not open
        return C
    if MyList[A] == MyList[C] and MyList[A] != MyList[B] and MyList[A] != " " and MyList[B] == " ":
        #Some ruling as above section
        #A and C are same, check if empty
        #if B is open, return it via
        return B
    if MyList[B] == MyList[C] and MyList[A] != MyList[B] and MyList[C] != " " and MyList[A] == " ":
        return A
    return -1

def printgrid(Grid): # Prints the grid out with all characters 0-8
    print("------")
    print("|" + str(Grid[0]) + "|" + str(Grid[1]) + "|" + str(Grid[2]) + "|")
    print("------")
    print("|" + str(Grid[3]) + "|" + str(Grid[4]) + "|" + str(Grid[5]) + "|")
    print("------")
    print("|" + str(Grid[6]) + "|" + str(Grid[7]) + "|" + str(Grid[8]) + "|")
    print("------")

LastMove = 0
FirstMove = 0
PlayerTurn = random.randint(1,2)
print(PlayerTurn)

turns = 1 # Tracks current turn of game
temp = input("How many games would you like the AI to have as practice? (Positive number) ")
WithoutPlay = int(temp) # Determines number of practice rounds AI gets

while turns < 10:

    

    if WithoutPlay <= 0:
        print("\n\n\n") # Spaces out grid during gameplay
        printgrid(grid)

    if turns % 2 == 0:
        if WithoutPlay <= 0:
            val = input("Player turn (Number 0 - 8):")
            temp = int(val)
            while grid[temp] != " ":
                val = input("Invalid move! Please enter another value")
                temp = int(val)
        else: # AI is still in practice games
            val = random.choice(Brain)
            temp = int(val)
            while grid[temp] != " ":
                temp = random.choice(Brain)
        grid[temp] = "O"
        LastMove = temp
        
    else:
        val = random.choice(Brain)
        temp = int(val)
        while grid[temp] != " ":
            temp = random.choice(Brain)

        if AICheck(grid, 0, 1, 2) != -1:
            temp = AICheck(grid, 0, 1, 2)
            if WithoutPlay <= 0:
                print("AI block action at location: ", temp)

        if AICheck(grid, 3, 4, 5) != -1:
            temp = AICheck(grid, 3, 4, 5)
            if WithoutPlay <= 0:
                print("AI block action at location: ", temp)

        if AICheck(grid, 6, 7, 8) != -1:
            temp = AICheck(grid, 6, 7, 8)
            if WithoutPlay <= 0:
                print("AI block action at location: ", temp)

        if AICheck(grid, 8, 5, 2) != -1:
            temp = AICheck(grid, 8, 5, 2)
            if WithoutPlay <= 0:
                print("AI block action at location: ", temp)

        if AICheck(grid, 0, 3, 6) != -1:
            temp = AICheck(grid, 0, 3, 6)
            if WithoutPlay <= 0:
                print("AI block action at location: ", temp)

        if AICheck(grid, 1, 4, 7) != -1:
            temp = AICheck(grid, 1, 4, 7)
            if WithoutPlay <= 0:
                print("AI block action at location: ", temp)

        if AICheck(grid, 0, 4, 8) != -1:
            temp = AICheck(grid, 0, 4, 8)
            if WithoutPlay <= 0:
                print("AI block action at location: ", temp)

        if AICheck(grid, 6, 4, 2) != -1:
            temp = AICheck(grid, 6, 4, 2)
            if WithoutPlay <= 0:
                print("AI block action at location: ", temp)

        LastMove = temp
        if turns == 1:
            FirstMove = temp
        
        grid[temp] = "X"


    if wincheck(grid, 0, 1, 2):
        winner = True
        turns = 10

    if wincheck(grid, 3, 4, 5):
        winner = True
        turns = 10

    if wincheck(grid, 6, 7, 8):
        winner = True
        turns = 10

    if wincheck(grid, 8, 5, 2):
        winner = True
        turns = 10

    if wincheck(grid, 0, 3, 6):
        winner = True
        turns = 10

    if wincheck(grid, 1, 4, 7):
        winner = True
        turns = 10

    if wincheck(grid, 0, 4, 8):
        winner = True
        turns = 10

    if wincheck(grid, 6, 4, 2):
        winner = True
        turns = 10

    

    turns += 1

    if turns > 9 and WithoutPlay <= 0:

        printgrid(grid)
        temp = input("Good game! Would you like to play again:")
        if temp == "Yes" or temp == "yes" or temp == "y":

            reset(grid)
            turns = 1                
            if winner is True:
                Brain.append(LastMove) 
                Brain.append(FirstMove)
                #print(Brain)
                winner = False
                ''' If player or AI wins, record first and last moves of game,
                giving AI weight towards player/victory decisions'''

    elif turns > 9:
        reset(grid)
        turns = 1
        WithoutPlay -= 1

        if winner:
            Brain.append(LastMove) # If player or AI wins, record first and last moves of game, giving AI weight towards player/victory decisions
            Brain.append(FirstMove)
            #print(Brain)
        winner = False

    
   
                    
'''Store the final move of a winning game in Brain using Brain.append(x), where x equals a value 0-8. At the end of any game,
use an if statement and see if a player would like to play again. If they do, reset turn count, clear the board, and
make sure loop is ready to run again.'''               
                
