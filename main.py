from collections import deque
from prettytable import PrettyTable
from node import Node
#https://tristanpenman.com/demos/n-puzzle/#
generatedStates =1 
expandedStates =0
goalState = ''

"""def solvable(initState):
    def getInvCount(arr):
        inv_count = 0
        for i in range(0, 9):
            for j in range(i + 1, 9):
                if arr[j] != '0' and arr[i] != '0' and arr[i] > arr[j]:
                    inv_count += 1
        return inv_count

    invCount = getInvCount(list(initState))
   return (invCount % 2 == 0)"""

def solveDFS(initState,goalState):
    global expandedStates
    global generatedStates
    queue = deque()
    path = [] 
    currentNode = Node(initState)
    while not currentNode.nIsGoal(goalState):
        ##print(currentNode.state)
        currentNode.expandNode()
        expandedStates += 1
        queue.extendleft(currentNode.children)
        generatedStates+=len(currentNode.children)
        currentNode = queue.pop()

    path.append(currentNode.state)
    for parent in currentNode.getParents():
        path.append(parent.state)
    path.reverse()

    return path

def printState(state):
    z=state.find('0')
    state = list(state)
    state[z]=" "
    stateTable= PrettyTable()
    stateTable.border = False
    stateTable.header = False
    stateTable.field_names = ["Col1","Col2","Col3"]
    stateTable.add_row([state[0],state[1],state[2]])
    stateTable.add_row([state[3],state[4],state[5]])
    stateTable.add_row([state[6],state[7],state[8]])
    print(stateTable)


def generateGoalState(state):
    goalState = sorted(state)
    goalState = ''.join(goalState)
    return goalState

def main():
    global generatedStates 
    global expandedStates 
    initialState = ""
    while(len(initialState)!=9):
        initialState = input("Please insert your 8 puzzle string:")
    
    printState(initialState)
    global goalState
    goalState = generateGoalState(initialState)
    printState(goalState)
    ##if(solvable(initialState)):
    path = solveDFS(initialState,goalState)
    for node in path:
        printState(node)
        print("\n"*2)
    print("Generated States:" + str(generatedStates)+"\n")
    print("Expanded States:" + str(expandedStates)+"\n")
    #else:
    #   print("cannot be solved")
    

if __name__ == "__main__":
    main()