#>> Ultimate Tic-Tac-Toe
#>> Daniel Walsh
#>> Code not to be used without written permission from Daniel Walsh.
#>> Credit must be given to Daniel Walsh if code is used once permission is given.
#>> Label control functions

def makeMove(labels, pos, turn):
    if(turn%2 == 0):
        labels[pos] = "X"
    else:
        labels[pos] = "O"

    return labels

