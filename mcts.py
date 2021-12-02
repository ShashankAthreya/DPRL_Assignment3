#%%
#import statements
import math
import numpy
from itertools import permutations

#%%
#Initilising TicTacToe as a 1D array
# 0|1|2
# 3|4|5
# 6|7|8

#%%
#Checking for winners
def anyWinner(array):
    if (array[0] == array[1] == array[2]) or (array[0] == array[3] == array[6]) or (array[0] == array[4] == array[8]):
        return (array[0])
    if (array[1] == array[4] == array[7]) or (array[3] == array[4] == array[5]) or (array[2] == array[4] == array[6]):
        return (array[4])
    if (array[6] == array[7] == array[8]) or (array[2] == array[5] == array[8]):
        return (array[4])
    return(None)

#%%
# Initialise lists and compute all possible games  
TicTacToe = ['','','','','','','','','']
currentOrder = [4,1,3,5]
playingOrder = []
allGames = []

openSpaces = permutations([0,2,6,7,8])

for i in openSpaces:
    order = []
    order.append(currentOrder)
    order.append(i)
    playingOrder.append(order)

for order in playingOrder:
    newGame = []
    for i in range(len(order)):
        if i%2==0:
            TicTacToe[order[i]] = 'X'
        else:
            TicTacToe[order[i]] = 'O'
    newGame.append(TicTacToe)
    allGames.append(newGame)

#%%
#Remove unfeasible states
