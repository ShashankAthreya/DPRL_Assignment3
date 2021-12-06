#%%
import numpy as np
import os
#initilaing tree class
class node(object):
    def __init__(self, value, children = [],curOrder = []):
        self.value = value
        self.children = children
        self.curOrder = curOrder
        self.terminal = False
        self.Q_value = None
        self.reward = 0
        self.parent = None
        self.n_visit = None

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return(str(self.value))

#initialising definitions
# '''
# 0|1|2
# 3|4|5
# 6|7|8
# '''
def anyWinner(array):
    if (array[0] == array[1] == array[2]) and array[0]!= '' and  array[1]!= '' and array[2]!='':
        return True
    if (array[0] == array[3] == array[6]) and array[0]!= '' and  array[3]!= '' and array[6]!='':
        return True
    if(array[0] == array[4] == array[8]) and array[0]!= '' and  array[4]!= '' and array[8]!='':
        return True
    if(array[1] == array[4] == array[7]) and array[1]!= '' and  array[4]!= '' and array[7]!='': 
        return True
    if(array[3] == array[4] == array[5]) and array[3]!= '' and  array[4]!= '' and array[5]!='':
        return True
    if(array[2] == array[4] == array[6]) and array[2]!= '' and  array[4]!= '' and array[6]!='':
        return True
    if (array[6] == array[7] == array[8]) and array[6]!= '' and  array[7]!= '' and array[8]!='':
        return True
    if(array[2] == array[5] == array[8]) and array[2]!= '' and  array[5]!= '' and array[8]!='':
        return True
    return False

def isTerminal(order):
    TicTacToe = ['','','','','','','','','']
    for i in range(len(order)):
        if i%2==0:
            TicTacToe[order[i]] = 'X'
        else:
            TicTacToe[order[i]] = 'O'
    if len(order) == 9 and anyWinner(TicTacToe) is False:
            return True
    if anyWinner(TicTacToe):
        return True
    return False

def T3(order):
    TicTacToe = ['','','','','','','','','']
    for i in range(len(order)):
        if i%2==0:
            TicTacToe[order[i]] = 'X'
        else:
            TicTacToe[order[i]] = 'O'
    return TicTacToe

def getReward(order):
    if len(order)%2==1:
        return(1.0)
    else:
        return(-1.0)

states = [x for x in range(9)]
def buidlTree(self):
    if isTerminal(self.curOrder):
        self.terminal = True
        if len(self.curOrder) == 9 and anyWinner(T3(self.curOrder)) is False:
            self.reward = -1.0
        else:
            self.reward = getReward(self.curOrder)
        self.Q_value = self.reward
        self.n_Visit = 1
        return
    else:
        self.children = [node(x) for x in states if x not in self.curOrder]
        for child in self.children:
            child.parent = self
            child.curOrder = child.parent.curOrder + [child.value]
            buidlTree(child)

def countSubNodes(self):
    if self.terminal:
        return 1
    nodeCount = len(self.children)
    for child in self.children:
        nodeCount += countSubNodes(child)
    return nodeCount

def calcQ(self):
    if self.terminal:
        return self.Q_value
    if self.Q_value is None:
        qValue = 0
        for child in self.children:
            if child.n_visit is None:
                child.n_visit = countSubNodes(child)
            if child.Q_value is None:
                child.Q_value = calcQ(child)
            qValue += ((child.reward + Gamma*child.Q_value)/child.n_visit)
        self.Q_value = qValue
        return qValue
#%%
def clearScreen():
    os.system('clear')
#%%
#Starting constrction of tree and hardcoding the starting state
#root node
Gamma = 1
# root = node(4)
root = node(5)
# initialNode = int(input("Player X: Starting State ->"))
# root = node(initialNode)
# root.curOrder= [root.value]
root.curOrder= [4,1,3,5]
# %%
# Completing the tree and calculating Q values
buidlTree(root)
print(calcQ(root))
clearScreen()
# %%
# Starting Game
players = ['X','O']
# curPlayer = 'X'
curPlayer = 'O'
curNode = root
while(not curNode.terminal):
    curPlayer = [x for x in players if x is not curPlayer][0]
    print("Current Player", curPlayer)
    curGame = T3(curNode.curOrder)
    for i in range(len(curGame)):
        print(curGame[i]," | ",end='')
        if(i%3==2 and i!=8):
            # print("\n---|---|---\n")
            print("\n")
        if (i==8):
            print("\n\n")
    qvalues = []
    for child in curNode.children:
        qvalues.append(child.Q_value)
        print(curNode.curOrder, child.value, child.Q_value)
    if curPlayer == 'X':
        optimalNode = curNode.children[np.argmax(qvalues)]
    if curPlayer == 'O':
        optimalNode = curNode.children[np.argmin(qvalues)]
    print("\nOptimal Node for player",curPlayer,"is: ", optimalNode.value)
    nextNode = int(input("Choose a node:"))
    try:
        index = [x for x in range(len(curNode.children)) if curNode.children[x].value == nextNode][0]
    except:
        print("Enter a vald state:")
        continue
    nextNode = curNode.children[index]
    curNode = nextNode
    clearScreen()

if curNode.terminal:
    curGame = T3(curNode.curOrder)
    for i in range(len(curGame)):
        print(curGame[i]," | ",end='')
        if(i%3==2 and i!=8):
            # print("\n---|---|---\n")
            print("\n")
        if (i==8):
            print("\n\n")
    if anyWinner(T3(curNode.curOrder)):
        winner = 'X' if len(curNode.curOrder)%2==1 else 'O'
        print("Player ",winner," wins")
    else:
        print("Draw")
# %%
