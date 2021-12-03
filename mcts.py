#%%
#initilaing tree class
class node(object):
    def __init__(self, value, children = [],curOrder = []):
        self.value = value
        self.children = children
        self.curOrder = curOrder
        self.terminal = False
        self.Q_value = None
        self.reward = None
        self.parent = None

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'

#initialising definitions
def anyWinner(array):
    print(array)
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
#%%
#Starting constrction of tree and hardcoding the starting state
#root node
root = node(4)
root.curOrder= [root.value]
root.children = [node(1)]
#child node
step2 = root.children[0]
step2.parent = root
step2.children = [node(3)]
step2.curOrder = step2.parent.curOrder + [step2.value]
#g-child
step3 = step2.children[0]
step3.parent = step2
step3.curOrder = step3.parent.curOrder + [step3.value]
step3.children = [node(5)]
#g2child
step4 = step3.children[0]
step4.parent = step3
step4.curOrder = step4.parent.curOrder + [step4.value]
step4.children = [node(0),node(1),node(6),node(7),node(8)]
# %%
# %%
