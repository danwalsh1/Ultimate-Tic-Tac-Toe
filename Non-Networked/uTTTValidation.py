#>> Ultimate Tic-Tac-Toe
#>> Daniel Walsh
#>> Code not to be used without written permission from Daniel Walsh.
#>> Credit must be given to Daniel Walsh if code is used once permission is given.
#>> Validation Functions

#################
### FUNCTIONS ###
#################

def checkOuterSquareCompleted(lblTL, lblTM, lblTR, lblML, lblMM, lblMR, lblBL, lblBM, lblBR):
    ''' This function returns a list of completed outer squares. 0 is incomplete, 1 is complete '''
    labelsBoard = [""] * 9
    
    result = checkWin(lblTL)
    if(result != "-"):
        labelsBoard[0] = result
    else:
        labelsBoard[0] = "0"

    result = checkWin(lblTM)
    if(result != "-"):
        labelsBoard[1] = result
    else:
        labelsBoard[1] = "0"

    result = checkWin(lblTR)
    if(result != "-"):
        labelsBoard[2] = result
    else:
        labelsBoard[2] = "0"

    result = checkWin(lblML)
    if(result != "-"):
        labelsBoard[3] = result
    else:
        labelsBoard[3] = "0"

    result = checkWin(lblMM)
    if(result != "-"):
        labelsBoard[4] = result
    else:
        labelsBoard[4] = "0"

    result = checkWin(lblMR)
    if(result != "-"):
        labelsBoard[5] = result
    else:
        labelsBoard[5] = "0"

    result = checkWin(lblBL)
    if(result != "-"):
        labelsBoard[6] = result
    else:
        labelsBoard[6] = "0"

    result = checkWin(lblBM)
    if(result != "-"):
        labelsBoard[7] = result
    else:
        labelsBoard[7] = "0"

    result = checkWin(lblBR)
    if(result != "-"):
        labelsBoard[8] = result
    else:
        labelsBoard[8] = "0"

    return labelsBoard

def checkWin(labels, size = 3):
    result = checkHor(labels, size)
    if(result == "X" or result == "O"):
        return result
    result = checkVer(labels, size)
    if(result == "X" or result == "O"):
        return result
    result = checkDia(labels, size)
    if(result == "X" or result == "O"):
        return result
    result = checkEnd(labels, size)
    if(result == "DRAW"):
        return result
    else:
        return "-"
    
def checkHor(labels, size):
    #>> Check rows for wins

    #>> Check for X win
    win = True
    count = 0
    while(count < size):
        count2 = count*size
        while(count2 < (count+1)*size):
            if(labels[count2] != "X" and win == True):
                win = False
            count2 += 1

        if(win == True):
            return "X"
        else:
            win = True
        count += 1
    #>> Check for O win
    win = True
    count = 0
    while(count < size):
        count2 = count*size
        while(count2 < (count+1)*size):
            if(labels[count2] != "O" and win == True):
                win = False
            count2 += 1

        if(win == True):
            return "O"
        else:
            win = True
        count += 1
    #>> No win has been found
    return "-"

def checkVer(labels, size):
    #>> Check columns for wins

    #>> Check for X win
    win = True
    count = 0
    while(count < size):
        count2 = 0
        while(count2 < size):
            #print(str(count+count2*size) + ":" + str(count) + ":" + str(count2))
            if(labels[count+count2*size] != "X" and win == True):
                win = False
            count2 += 1
        if(win == True):
            return "X"
        else:
            win = True
        count += 1
    #>> Check for O win
    win = True
    count = 0
    while(count < size):
        count2 = 0
        while(count2 < size):
            if(labels[count+count2*size] != "O" and win == True):
                win = False
            count2 += 1
        if(win == True):
            return "O"
        else:
            win = True
        count += 1
    #>> No win has been found
    return "-"

def checkDia(labels, size):
    #>> Check diagonals for wins

    #>> Top left to bottom right
    #>> Check for X win
    win = True
    count = 0
    while(count < size):
        if(labels[count*size+count] != "X" and win == True):
            win = False
        count += 1
    if(win == True):
        return "X"
    #>> Check for O win
    win = True
    count = 0
    while(count < size):
        if(labels[count*size+count] != "O" and win == True):
            win = False
        count += 1
    if(win == True):
        return "O"
    #>> Top right to bottom left
    #>> Check for X win
    win = True
    count = 0
    while(count < size):
        if(labels[(size-1)*(count+1)] != "X" and win == True):
            win = False
        count += 1
    if(win == True):
        return "X"
    #>> Check for O win
    win = True
    count = 0
    while(count < size):
        if(labels[(size-1)*(count+1)] != "O" and win == True):
            win = False
        count += 1
    if(win == True):
        return "O"
    
    
    return "-"

def checkEnd(labels, size):
    ''' This function is used to check if the game has ended in a draw '''
    count = 0
    while(count < size**2):
        if(labels[count] != "X" and labels[count] != "O"):
            #>> Game has not ended in a draw yet
            return "-"
        count += 1
    #>> Game has ended in a draw
    return "DRAW"

def getBasePosition(pos):
    while(pos > 8):
        pos -= 9

    return pos

def validatePosition(labels, pos):
    pos = getBasePosition(pos)
    if(labels[pos] == "X" or labels[pos] == "Y"):
        return False
    else:
        return True
