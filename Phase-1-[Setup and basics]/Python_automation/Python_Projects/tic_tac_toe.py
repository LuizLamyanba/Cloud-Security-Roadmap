board = {'TL': ' ','TM':' ','TR':' ', 'ML': ' ', 'M': ' ', 'MR':' ','LF': ' ','L':' ','LR':' ' }

def printboard(board):
    print(board['TL']+' | '+board['TM']+'| '+board['TR'])
    print('--+--+--')
    print(board['ML']+' | '+board['M']+'| '+board['MR'])
    print('--+--+--')
    print(board['LF']+' | '+board['L']+'| '+board['LR'])


def wincond(turn,play):
    if  board['TL'] == board['TM'] == board['TR'] != " ": #
        print(play + " who chose "+turn+" wins")
        return True

    elif  board['TL'] == board['ML'] == board['LF'] != " ": #
        print(play + " who chose "+turn+" wins")
        return True
    
    elif  board['LF'] == board['L'] == board['LR'] != " " :  #
        print(play + " who chose "+turn+" wins")
        return True
    
    elif  board['TR'] == board['MR'] == board['LR'] != " " : #
        print(play + " who chose "+turn+" wins")
        return True
    
    elif  board['LR'] == board['M'] == board['MR'] != " " :  #
        print(play + " who chose "+turn+" wins")
        return True
    
    elif  board['TM'] == board['M'] == board['L'] != " ":  #
        print(play + " who chose "+turn+" wins")
        return True
    
    elif  board['LF'] == board['M'] == board['TR'] != " ":
        print(play + " who chose "+turn+" wins")
        return True
    
    elif  board['TL'] == board['M'] == board['LR'] != " " :
        print(play + " who chose "+turn+" wins")
        return True
    else:
        return False

def main():
    print('-----------WELCOME TO TIC TACE TOE------------')
    turn = 'X'
    play = 'player 1'
    for i in range(9):
        printboard(board)
        move = input((play+' your chance,select positon for where you want to place '+turn+' : '))
        board[move] = turn
        if wincond(turn,play):
            print()
            printboard(board)
            break
        
        if turn == 'X' and play == 'player 1':
            turn = 'O'
            play = 'player 2'
        else:
            turn ='X'
            play = 'player 1'
main()    


 
