from collections import deque
from prettytable import PrettyTable
from node import Node

generatedStates =1 
expandedStates =0
goalState = ''

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

    path.append(currentNode)
    for parent in currentNode.getParents():
        path.append(parent)
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
    actions = []
    while(len(initialState)!=9):
        initialState = input("Please insert your 8 puzzle string:")
    
    printState(initialState)
    global goalState
    goalState = generateGoalState(initialState)
    printState(goalState)
    path = solveDFS(initialState,goalState)
    for node in path:
        printState(node.state)
        print("\n"*2)
        actions.append(node.action)

    print ("Actions:" + str(actions)[5:-1] )

    print("Generated States:" + str(generatedStates))
    print("Expanded States:" + str(expandedStates))
    

if __name__ == "__main__":
    main()