#>> Ultimate Tic-Tac-Toe
#>> Daniel Walsh
#>> Code not to be used without written permission from Daniel Walsh.
#>> Credit must be given to Daniel Walsh if code is used once permission is given.
#>> Button Positions Functions

#################
### FUNCTIONS ###
#################

def getButtonSquare(btnNum):
    #>> btnNum = 0 to 80 (inclusive)
    #>> 1 2 3
    #>> 4 5 6
    #>> 7 8 9
    if(btnNum < 9):
        return 1
    elif(btnNum < 18):
        return 2
    elif(btnNum < 27):
        return 3
    elif(btnNum < 36):
        return 4
    elif(btnNum < 45):
        return 5
    elif(btnNum < 54):
        return 6
    elif(btnNum < 63):
        return 7
    elif(btnNum < 72):
        return 8
    else:
        return 9

def getButtonInnerSquare(btnNum):
    #>> btnNum = 0 to 80 (inclusive)
    #>> 1 2 3
    #>> 4 5 6
    #>> 7 8 9
    while(btnNum > 8):
        btnNum -= 9

    if(btnNum == 0):
        return 1
    elif(btnNum == 1):
        return 2
    elif(btnNum == 2):
        return 3
    elif(btnNum == 3):
        return 4
    elif(btnNum == 4):
        return 5
    elif(btnNum == 5):
        return 6
    elif(btnNum == 6):
        return 7
    elif(btnNum == 7):
        return 8
    elif(btnNum == 8):
        return 9
