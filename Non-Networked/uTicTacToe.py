#>> Ultimate Tic-Tac-Toe
#>> Daniel Walsh
#>> Code not to be used without written permission from Daniel Walsh.
#>> Credit must be given to Daniel Walsh if code is used once permission is given.

###############
### IMPORTS ###
###############

import tkinter as tk
import tkinter.font
import tkinter.messagebox
from functools import partial
from uTTTButtonPositions import getButtonSquare, getButtonInnerSquare
from uTTTValidation import checkOuterSquareCompleted, validatePosition, getBasePosition, checkWin
from uTTTLabelControl import makeMove

###############
### GLOBALS ###
###############

labelsTL = [""] * 9
labelsTM = [""] * 9
labelsTR = [""] * 9
labelsML = [""] * 9
labelsMM = [""] * 9
labelsMR = [""] * 9
labelsBL = [""] * 9
labelsBM = [""] * 9
labelsBR = [""] * 9
labelsBoard = ["0", "0", "0", "0", "0", "0", "0", "0", "0"]

gameState = "PLAYING"
turn = 0
nextOuterSquare = -1

btnHeight = 2
btnWidth = 5
initialText = ""
systemColour = "light grey"
playerOneColour = "light blue"
playerTwoColour = "light green"
drawColour = "red"

#################
### FUNCTIONS ###
#################

def updateBoard(updateType, info = ""):
    #>> Globals
    global buttons
    
    if(updateType == "WIN"):
        #>> Only update lblInfo to show who won
        if(info == "DRAW"):
            lblInfo.configure(text = "The game has ended in a draw!")
        else:
            lblInfo.configure(text = "Player " + info + " has won!")
    else:
        if(updateType == "0"):
            #>> Update outer square 1
            for num in range(0, 9):
                buttons[num].config(text = labelsTL[num])
        elif(updateType == "1"):
            #>> Update outer square 2
            for num in range(0, 9):
                buttons[num+9].config(text = labelsTM[num])
        elif(updateType == "2"):
            #>> Update outer square 3
            for num in range(0, 9):
                buttons[num+18].config(text = labelsTR[num])
        elif(updateType == "3"):
            #>> Update outer square 4
            for num in range(0, 9):
                buttons[num+27].config(text = labelsML[num])
        elif(updateType == "4"):
            #>> Update outer square 5
            for num in range(0, 9):
                buttons[num+36].config(text = labelsMM[num])
        elif(updateType == "5"):
            #>> Update outer square 6
            for num in range(0, 9):
                buttons[num+45].config(text = labelsMR[num])
        elif(updateType == "6"):
            #>> Update outer square 7
            for num in range(0, 9):
                buttons[num+54].config(text = labelsBL[num])
        elif(updateType == "7"):
            #>> Update outer square 8
            for num in range(0, 9):
                buttons[num+63].config(text = labelsBM[num])
        elif(updateType == "8"):
            #>> Update outer square 9
            for num in range(0, 9):
                buttons[num+72].config(text = labelsBR[num])

        #>> Update lblInfo to display who's turn it is
        if(turn%2 == 0):
            lblInfo.configure(text = "Player 1's turn!")
        else:
            lblInfo.configure(text = "Player 2's turn!")
        
def uValidatePosition(pos):
    if(nextOuterSquare == 0):
        return validatePosition(labelsTL, pos)
    elif(nextOuterSquare == 1):
        return validatePosition(labelsTM, pos)
    elif(nextOuterSquare == 2):
        return validatePosition(labelsTR, pos)
    elif(nextOuterSquare == 3):
        return validatePosition(labelsML, pos)
    elif(nextOuterSquare == 4):
        return validatePosition(labelsMM, pos)
    elif(nextOuterSquare == 5):
        return validatePosition(labelsMR, pos)
    elif(nextOuterSquare == 6):
        return validatePosition(labelsBL, pos)
    elif(nextOuterSquare == 7):
        return validatePosition(labelsBM, pos)
    elif(nextOuterSquare == 8):
        return validatePosition(labelsBR, pos)

def uMakeMove(pos):
    if(getButtonSquare(pos) == 1):
        global labelsTL
        labelsTL = makeMove(labelsTL, getBasePosition(pos), turn)
    elif(getButtonSquare(pos) == 2):
        global labelsTM
        labelsTM = makeMove(labelsTM, getBasePosition(pos), turn)
    elif(getButtonSquare(pos) == 3):
        global labelsTR
        labelsTR = makeMove(labelsTR, getBasePosition(pos), turn)
    elif(getButtonSquare(pos) == 4):
        global labelsML
        labelsML = makeMove(labelsML, getBasePosition(pos), turn)
    elif(getButtonSquare(pos) == 5):
        global labelsMM
        labelsMM = makeMove(labelsMM, getBasePosition(pos), turn)
    elif(getButtonSquare(pos) == 6):
        global labelsMR
        labelsMR = makeMove(labelsMR, getBasePosition(pos), turn)
    elif(getButtonSquare(pos) == 7):
        global labelsBL
        labelsBL = makeMove(labelsBL, getBasePosition(pos), turn)
    elif(getButtonSquare(pos) == 8):
        global labelsBM
        labelsBM = makeMove(labelsBM, getBasePosition(pos), turn)
    elif(getButtonSquare(pos) == 9):
        global labelsBR
        labelsBR = makeMove(labelsBR, getBasePosition(pos), turn)

def dehighlight(pos):
    #>> Globals
    global buttons
    
    if(getButtonSquare(pos) == 1):
        for num in range(0, 9):
            buttons[num].config(bg = "SystemButtonFace")
    elif(getButtonSquare(pos) == 2):
        for num in range(9, 18):
            buttons[num].config(bg = "SystemButtonFace")
    elif(getButtonSquare(pos) == 3):
        for num in range(18, 27):
            buttons[num].config(bg = "SystemButtonFace")
    elif(getButtonSquare(pos) == 4):
        for num in range(27, 36):
            buttons[num].config(bg = "SystemButtonFace")
    elif(getButtonSquare(pos) == 5):
        for num in range(36, 45):
            buttons[num].config(bg = "SystemButtonFace")
    elif(getButtonSquare(pos) == 6):
        for num in range(45, 54):
            buttons[num].config(bg = "SystemButtonFace")
    elif(getButtonSquare(pos) == 7):
        for num in range(54, 63):
            buttons[num].config(bg = "SystemButtonFace")
    elif(getButtonSquare(pos) == 8):
        for num in range(63, 72):
            buttons[num].config(bg = "SystemButtonFace")
    elif(getButtonSquare(pos) == 9):
        for num in range(72, 81):
            buttons[num].config(bg = "SystemButtonFace")

def highlight(pos, colour = "gold"):
    #>> Globals
    global buttons
    
    if(pos == 0):
        for num in range(0, 9):
            buttons[num].config(bg = colour)
    elif(pos == 1):
        for num in range(9, 18):
            buttons[num].config(bg = colour)
    elif(pos == 2):
        for num in range(18, 27):
            buttons[num].config(bg = colour)
    elif(pos == 3):
        for num in range(27, 36):
            buttons[num].config(bg = colour)
    elif(pos == 4):
        for num in range(36, 45):
            buttons[num].config(bg = colour)
    elif(pos == 5):
        for num in range(45, 54):
            buttons[num].config(bg = colour)
    elif(pos == 6):
        for num in range(54, 63):
            buttons[num].config(bg = colour)
    elif(pos == 7):
        for num in range(63, 72):
            buttons[num].config(bg = colour)
    elif(pos == 8):
        for num in range(72, 81):
            buttons[num].config(bg = colour)
    

def btnPress(btnNum):
    #>> Globals
    global labelsBoard
    global turn
    global nextOuterSquare
    global gameState
    global buttons

    if(gameState != "PLAYING"):
        return None

    #>> Is this position in the correct outer square?
    if(nextOuterSquare != -1):
        #>> Check if the position is in the valid outer square
        if(nextOuterSquare != getButtonSquare(btnNum)-1):
            #>> Not a valid position
            tk.messagebox.showwarning("Invalid Move", "Select a position in the valid square set!")
            return None
    else:
        if(labelsBoard[getButtonSquare(btnNum)-1] != "0"):
            #>> Outer square already completed
            tk.messagebox.showwarning("Invalid Move", "Select a position in a square that hasn't been completed")
            return None

    #>> Is the selected position already taken?
    result = uValidatePosition(btnNum)
    if(result == False):
        #>> Not a valid position
        tk.messagebox.showwarning("Invalid Move", "Select a position that hasn't already been taken!")
        return None

    #>> Make move
    uMakeMove(btnNum)

    #>> De-highlight the next outer square
    dehighlight(btnNum)
    
    #>> Calculate and store next outer square
    currOuterSquare = nextOuterSquare
    nextOuterSquare = getBasePosition(btnNum)
    
    #>> Update labelsBoard
    labelsBoard = checkOuterSquareCompleted(labelsTL, labelsTM, labelsTR, labelsML, labelsMM, labelsMR, labelsBL, labelsBM, labelsBR)
    
    #>> Check if all outer squares have been completed
    allComplete = True
    for num in range(0, 9):
        if(labelsBoard[num] == "0"):
            allComplete = False
    if(allComplete == True):
        #>> Game Over!
        #>> Check for win/draw
        #>> Output result & end game
        result = checkWin(labelsBoard)
        if(result == "X"):
            updateBoard("WIN", "1")
        elif(result == "O"):
            updateBoard("WIN", "1")
        else:
            updateBoard("WIN", "DRAW")
        #>> Outer square is completed
        #>> Find and show winner of the outer square
        if(labelsBoard[getButtonSquare(btnNum)-1] == "X"):
            highlight(getButtonSquare(btnNum)-1, playerOneColour)
        elif(labelsBoard[getButtonSquare(btnNum)-1] == "O"):
            highlight(getButtonSquare(btnNum)-1, playerTwoColour)
        else:
            highlight(getButtonSquare(btnNum)-1, drawColour)
        gameState = "GAME OVER"
        return None

    #>> Check if a win of outer squares has been made
    result = checkWin(labelsBoard)
    if(result != "-"):
        #>> Game has finished
        if(result == "X"):
            updateBoard("WIN", "1")
        elif(result == "O"):
            updateBoard("WIN", "1")
        else:
            updateBoard("WIN", "DRAW")
        #>> Outer square is completed
        #>> Find and show winner of the outer square
        if(labelsBoard[getButtonSquare(btnNum)-1] == "X"):
            highlight(getButtonSquare(btnNum)-1, playerOneColour)
        elif(labelsBoard[getButtonSquare(btnNum)-1] == "O"):
            highlight(getButtonSquare(btnNum)-1, playerTwoColour)
        else:
            highlight(getButtonSquare(btnNum)-1, drawColour)
        #>> Update the current button text
        if(turn%2 == 0):
            buttons[btnNum].configure(text = "X")
        else:
            buttons[btnNum].configure(text = "O")
        #>> Set the game to finished
        gameState = "GAME OVER"
        return None
    
    #>> Check if next outer square has been complteted and curr outer square
    if(labelsBoard[getButtonSquare(btnNum)-1] != "0"):
        #>> Outer square is completed
        #>> Find and show winner of the outer square
        if(labelsBoard[getButtonSquare(btnNum)-1] == "X"):
            highlight(getButtonSquare(btnNum)-1, playerOneColour)
        elif(labelsBoard[getButtonSquare(btnNum)-1] == "O"):
            highlight(getButtonSquare(btnNum)-1, playerTwoColour)
        else:
            highlight(getButtonSquare(btnNum)-1, drawColour)
    
    if(labelsBoard[nextOuterSquare] != "0"):
        #>> Outer square is completed
        #>> Player may choose any outer square
        nextOuterSquare = -1
    else:
        #>> Highlight the next outer square
        highlight(nextOuterSquare)
    
    #>> Update turn
    turn += 1
    
    #>> Update board
    updateBoard(str(getButtonSquare(btnNum)-1))

###########
### GUI ###
###########

root = tk.Tk()

root.configure(background = systemColour)
root.resizable(0,0)

root.title("Ultimate Tic-Tac-Toe")

buttons = []
for num in range(0, 81):
    button = tk.Button(root, text = initialText, height = btnHeight, width = btnWidth, command = lambda num = num: btnPress(num))
    buttons.append(button)

buttons[0].grid(row = 0, column = 0)
buttons[1].grid(row = 0, column = 1)
buttons[2].grid(row = 0, column = 2)
buttons[3].grid(row = 1, column = 0)
buttons[4].grid(row = 1, column = 1)
buttons[5].grid(row = 1, column = 2)
buttons[6].grid(row = 2, column = 0)
buttons[7].grid(row = 2, column = 1)
buttons[8].grid(row = 2, column = 2)

lbl1 = tk.Label(root, text = " ", font = ("Helvetica", 13), bg = systemColour)
lbl1.grid(row = 0, column = 3)

buttons[9].grid(row = 0, column = 4)
buttons[10].grid(row = 0, column = 5)
buttons[11].grid(row = 0, column = 6)
buttons[12].grid(row = 1, column = 4)
buttons[13].grid(row = 1, column = 5)
buttons[14].grid(row = 1, column = 6)
buttons[15].grid(row = 2, column = 4)
buttons[16].grid(row = 2, column = 5)
buttons[17].grid(row = 2, column = 6)

lbl2 = tk.Label(root, text = " ", font = ("Helvetica", 13), bg = systemColour)
lbl2.grid(row = 0, column = 7)

buttons[18].grid(row = 0, column = 8)
buttons[19].grid(row = 0, column = 9)
buttons[20].grid(row = 0, column = 10)
buttons[21].grid(row = 1, column = 8)
buttons[22].grid(row = 1, column = 9)
buttons[23].grid(row = 1, column = 10)
buttons[24].grid(row = 2, column = 8)
buttons[25].grid(row = 2, column = 9)
buttons[26].grid(row = 2, column = 10)

lbl3 = tk.Label(root, text = " ", font = ("Helvetica", 13), bg = systemColour)
lbl3.grid(row = 3, column = 0)

buttons[27].grid(row = 4, column = 0)
buttons[28].grid(row = 4, column = 1)
buttons[29].grid(row = 4, column = 2)
buttons[30].grid(row = 5, column = 0)
buttons[31].grid(row = 5, column = 1)
buttons[32].grid(row = 5, column = 2)
buttons[33].grid(row = 6, column = 0)
buttons[34].grid(row = 6, column = 1)
buttons[35].grid(row = 6, column = 2)

buttons[36].grid(row = 4, column = 4)
buttons[37].grid(row = 4, column = 5)
buttons[38].grid(row = 4, column = 6)
buttons[39].grid(row = 5, column = 4)
buttons[40].grid(row = 5, column = 5)
buttons[41].grid(row = 5, column = 6)
buttons[42].grid(row = 6, column = 4)
buttons[43].grid(row = 6, column = 5)
buttons[44].grid(row = 6, column = 6)

buttons[45].grid(row = 4, column = 8)
buttons[46].grid(row = 4, column = 9)
buttons[47].grid(row = 4, column = 10)
buttons[48].grid(row = 5, column = 8)
buttons[49].grid(row = 5, column = 9)
buttons[50].grid(row = 5, column = 10)
buttons[51].grid(row = 6, column = 8)
buttons[52].grid(row = 6, column = 9)
buttons[53].grid(row = 6, column = 10)

lbl4 = tk.Label(root, text = " ", font = ("Helvetica", 13), bg = systemColour)
lbl4.grid(row = 7, column = 0)

buttons[54].grid(row = 8, column = 0)
buttons[55].grid(row = 8, column = 1)
buttons[56].grid(row = 8, column = 2)
buttons[57].grid(row = 9, column = 0)
buttons[58].grid(row = 9, column = 1)
buttons[59].grid(row = 9, column = 2)
buttons[60].grid(row = 10, column = 0)
buttons[61].grid(row = 10, column = 1)
buttons[62].grid(row = 10, column = 2)

buttons[63].grid(row = 8, column = 4)
buttons[64].grid(row = 8, column = 5)
buttons[65].grid(row = 8, column = 6)
buttons[66].grid(row = 9, column = 4)
buttons[67].grid(row = 9, column = 5)
buttons[68].grid(row = 9, column = 6)
buttons[69].grid(row = 10, column = 4)
buttons[70].grid(row = 10, column = 5)
buttons[71].grid(row = 10, column = 6)

buttons[72].grid(row = 8, column = 8)
buttons[73].grid(row = 8, column = 9)
buttons[74].grid(row = 8, column = 10)
buttons[75].grid(row = 9, column = 8)
buttons[76].grid(row = 9, column = 9)
buttons[77].grid(row = 9, column = 10)
buttons[78].grid(row = 10, column = 8)
buttons[79].grid(row = 10, column = 9)
buttons[80].grid(row = 10, column = 10)

lblP1 = tk.Label(root, text="Player 1", bg = playerOneColour)
lblP1.grid(row = 11, column = 0, columnspan = 3)
lblInfo = tk.Label(root, text = "Player 1's Turn", bg = systemColour)
lblInfo.grid(row = 11, column = 4, columnspan = 3)
lblP2 = tk.Label(root, text="Player 2", bg = playerTwoColour)
lblP2.grid(row = 11, column = 8, columnspan = 3)

root.mainloop()

############
### GAME ###
############

while(True):
    #>> Play the game

    endGame = input("End game? [Y/N]: ")
    if(endGame == "Y" or endGame == "y"):
        break
