board=[' ' for i in range(10)]

def clearBoard():
    for i in range(10):
        board[i]=' '

def showBoard(board):
    print('   |   |')
    print(' ' +board[1] + ' | ' + board[2]+ ' |  ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' +board[4] + ' | ' + board[5]+ ' |  ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' +board[7] + ' | ' + board[8]+ ' |  ' + board[9])
    print('   |   |')
    
def isSpaceFree(pos):
    return board[pos]==' '

def isWinner(b,l):
    return (b[1]==l and b[2]==l and b[3]==l) or (b[4]==l and b[5]==l and b[6]==l) or (b[7]==l and b[8]==l and b[9]==l) or(b[1]==l and b[4]==l and b[7]==l) or (b[2]==l and b[5]==l and b[8]==l) or (b[3]==l and b[6]==l and b[9]==l) or(b[1]==l and b[5]==l and b[9]==l) or (b[3]==l and b[5]==l and b[7]==l) 

def addLetter(pos, l):
    board[pos]=l
    
def isBoardFull(board):
    if board.count(' ')>1:
        return False
    else:
        return True

def playerMove():
    run=True
    while run:    
        pos=input("Enter the position where you want to enter X: ")
        try:
            pos=int(pos)
            if 0<pos and pos<10:        
                if(isSpaceFree(pos)):
                    addLetter(pos, 'X')
                    run=False
                else:
                    print("Enter a number in the valid range (1-9)")
            else:
                print("The space has been alredy occupied")
        except:
            print("Enter a number")
            
def computerMove():
    move=0
    possibleMoves= [x for x, letter in enumerate(board) if letter==' ' and x!=0]
    print(possibleMoves)
    print("\n")
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy=board[:]
            boardCopy[i]= let
            if isWinner(boardCopy,let):
                move =i
                return move
    corners=[]
    for i in possibleMoves:
        if i==1 or i==3 or i==7 or i==9:
            corners.append(i)
            
    if len(corners)>0:
        move = randomInd(corners)
        return move
    
    if 5 in possibleMoves:
        move =5
        return move
    
    edges=[]
    for i in possibleMoves:
        if i==2 or i==4 or i==6 or i==8:
            edges.append(i)
            
    if len(edges)>0:
        move = randomInd(edges)
    return move
    
def randomInd(li):
    import random
    l=len(li)
    r=random.randrange(0,l)
    return li[r]


    
def main():
    showBoard(board)
    while not(isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            showBoard(board)
        else:
            print("You lost ;P")
            break
        if not(isWinner(board, 'X')):
            move=computerMove()
            if move==0:
                print("Tie Game")
            else:
                addLetter(move, 'O')
                print("Computer placed an O in position ", move, " :")
                showBoard(board)
        else:
            print("Congrats, you won")
            break
    if isBoardFull(board):
        print("Tie game")

ch='y'
while ch=='y' or ch=='Y':    
    main()
    clearBoard()
    ch=input ("Do you want t ocontinue (y/n)")
          