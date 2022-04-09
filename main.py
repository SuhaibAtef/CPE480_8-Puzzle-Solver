from collections import deque
from secrets import choice
from prettytable import PrettyTable
from node import Node

generatedStates =1 
expandedStates =0
goalState = ''

def solveDFS(initState,goalState,choice):
    global expandedStates
    global generatedStates
    queue = deque()
    path = [] 
    currentNode = Node(initState)

    if (currentNode.nIsGoal(goalState)):
        path.append(currentNode)
        return path

    if (choice==1):
        while not currentNode.nIsGoal(goalState) :
            #print(currentNode.state)
                currentNode.expandNode()
                expandedStates += 1
                generatedStates+=len(currentNode.children)
                for child in currentNode.children:
                    if(child.nIsGoal(goalState)):
                        path.append(child)
                        for parent in child.getParents():
                            path.append(parent)
                        path.reverse()
                        return path
                queue.extendleft(currentNode.children)
                currentNode = queue.pop()
    
    if (choice==2):
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
    choice =-1
    while(len(initialState)!=9):
        initialState = input("Please insert your 8 puzzle string:")
    while(choice!=1 and choice!=2):
        choice = int(input("1: Test at node generation 2: Test at node expanding, what's your choice?"))
    print("===== Initial State =====")
    printState(initialState)
    print("===== ===== ===== =====\n")
    global goalState
    goalState = generateGoalState(initialState)
    print("===== Goal State =====")
    printState(goalState)
    print("===== ===== ===== =====\n")

    print("======= Moves =======\n")
    
    path = solveDFS(initialState,goalState,choice)
    for node in path:
        printState(node.state)
        print("\n"*2)
        actions.append(node.action)
    print("===== ===== ===== =====")
    print ("Actions:" + str(actions)[5:-1] )
    print("Generated States:" + str(generatedStates))
    print("Expanded States:" + str(expandedStates))
    

if __name__ == "__main__":
    main()