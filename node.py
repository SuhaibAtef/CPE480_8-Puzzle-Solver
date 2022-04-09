def stateInAction(state,parent):
    ActionsAllowed = []
    zeroPosition = state.find('0')
    def ActionRight(state,index):
        state = list(state)
        newState = state.copy()
        newState[index] = state[index+1]
        newState[index+1] = state[index]
        newState = "".join(newState)
        ActionsAllowed.append(Node(newState, parent, parent.depth + 1,"Right"))   
        
    def ActionLeft(state,index):
        state = list(state)
        newState = state.copy()
        newState[index] = state[index-1]
        newState[index-1] = state[index]
        newState = "".join(newState)
        ActionsAllowed.append(Node(newState, parent, parent.depth + 1,"Left")) 

    def ActionUp(state,index):
        state = list(state)
        newState = state.copy()
        newState[index] = state[index-3]
        newState[index-3] = state[index]
        newState = "".join(newState)
        ActionsAllowed.append(Node(newState, parent, parent.depth + 1,"Up")) 

    def ActionDown(state,index):
        state = list(state)
        newState = state.copy()
        newState[index] = state[index+3]
        newState[index+3] = state[index]
        newState = "".join(newState)
        ActionsAllowed.append(Node(newState, parent, parent.depth + 1,"Down")) 

    if(zeroPosition!=0 and zeroPosition!=1 and zeroPosition!=2):
        ActionUp(state,zeroPosition)

    if(zeroPosition!=6 and zeroPosition!=7 and zeroPosition!=8):
        ActionDown(state,zeroPosition)
        
    if(zeroPosition!=2 and zeroPosition!=5 and zeroPosition!=8):
        ActionRight(state,zeroPosition)

    if(zeroPosition!=0 and zeroPosition!=3 and zeroPosition!=6):
        ActionLeft(state,zeroPosition)

    return ActionsAllowed
    

def isGoal(state,goalState):
    for i in range(len(state)):
            if state[i] != goalState[i]:
                return False
    return True


class Node:

    def __init__(self, state=None,parent=None,depth=0,action="",children=[]):
      self.state = state
      self.parent = parent
      self.depth = depth
      self.children = children
      self.action = action

    def getState(self):
        return self.state

    def nIsGoal(self,goalState):
        return isGoal(self.state, goalState)

    def expandNode(self):
        self.children = stateInAction(str(self.state),self)

    def getParents(self):
        currentNode = self
        while currentNode.parent:
            yield currentNode.parent
            currentNode = currentNode.parent



