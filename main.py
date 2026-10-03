import random
import time
from queue import PriorityQueue
class Node:
    def __init__(self, state, parent=None, action=None, pathCost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.pathCost = pathCost

    def childNode(self, action):
        offsets = {"Up": -3, "Down": 3, "Left": -1, "Right": 1}
        i = self.state.index(0) 
        j = i + offsets[action] 
        newState = list(self.state)
        temp = newState[i]
        newState[i] = newState[j]
        newState[j] = temp

        return Node(newState, self, action, self.pathCost + 1)
    # magic function for less than to avoid the issue of comparing two values that are the same in the priority queue, returns false to say neither node is smaller.
    def __lt__(self, other):
        return False
    
def generatePuzzle():
    depthIndex = random.randint(0,4)
    puzzleIndex = random.randint(0,9)
    puzzleDepth4to20 = [ 
    [[1, 2, 5, 3, 4, 8, 6, 7, 0],
    [1, 2, 5, 3, 0, 4, 6, 7, 8],
    [1, 4, 2, 6, 3, 5, 0, 7, 8],
    [1, 4, 0, 3, 5, 2, 6, 7, 8],
    [1, 4, 2, 3, 5, 8, 6, 7, 0],
    [1, 4, 2, 3, 7, 5, 0, 6, 8],
    [1, 4, 2, 3, 7, 5, 6, 8, 0],
    [0, 3, 2, 4, 1, 5, 6, 7, 8],
    [3, 2, 0, 4, 1, 5, 6, 7, 8],
    [3, 1, 0, 4, 5, 2, 6, 7, 8],],

    [[1, 2, 5, 4, 0, 8, 3, 6, 7],
    [2, 3, 5, 1, 0, 4, 6, 7, 8],
    [1, 4, 2, 6, 0, 3, 7, 8, 5],
    [1, 5, 4, 6, 3, 2, 0, 7, 8],
    [1, 2, 0, 3, 4, 8, 6, 5, 7],
    [4, 7, 2, 1, 0, 5, 3, 6, 8],
    [1, 7, 4, 3, 0, 2, 6, 8, 5],
    [0, 4, 2, 1, 3, 5, 6, 7, 8],
    [3, 2, 5, 4, 0, 8, 6, 1, 7],
    [4, 3, 1, 5, 0, 2, 6, 7, 8],],

    [[0, 2, 5, 1, 6, 8, 4, 3, 7],
    [0, 3, 5, 2, 7, 4, 1, 6, 8],
    [4, 2, 0, 1, 6, 3, 7, 8, 5],
    [1, 5, 4, 6, 0, 3, 7, 8, 2],
    [1, 2, 8, 3, 0, 7, 6, 4, 5],
    [4, 7, 2, 1, 5, 8, 0, 3, 6],
    [1, 7, 4, 6, 0, 2, 8, 3, 5],
    [1, 4, 2, 6, 3, 5, 7, 8, 0],
    [3, 5, 8, 4, 0, 2, 6, 1, 7],
    [5, 4, 1, 6, 3, 2, 0, 7, 8],],

    [[2, 6, 5, 1, 8, 7, 4, 3, 0],
    [3, 7, 5, 2, 4, 8, 1, 6, 0],
    [4, 2, 3, 1, 8, 6, 7, 5, 0],
    [1, 5, 4, 6, 0, 8, 7, 2, 3],
    [1, 8, 7, 3, 0, 2, 6, 4, 5],
    [4, 7, 2, 5, 8, 6, 1, 3, 0],
    [1, 7, 4, 8, 6, 2, 3, 5, 0],
    [1, 3, 4, 6, 0, 2, 7, 8, 5],
    [3, 5, 8, 6, 0, 2, 1, 4, 7],
    [5, 4, 1, 6, 0, 3, 7, 8, 2],],

    [[2, 6, 5, 8, 0, 7, 1, 4, 3],
    [3, 7, 5, 1, 2, 8, 0, 4, 6],
    [0, 4, 3, 1, 2, 8, 7, 5, 6],
    [5, 6, 4, 1, 0, 8, 7, 2, 3],
    [8, 7, 0, 1, 3, 2, 6, 4, 5],
    [4, 7, 2, 8, 0, 6, 5, 1, 3],
    [0, 1, 4, 8, 7, 6, 3, 5, 2],
    [1, 3, 4, 6, 0, 8, 7, 5, 2],
    [5, 8, 0, 3, 6, 2, 1, 4, 7],
    [5, 4, 1, 7, 6, 3, 8, 2, 0],]
    ]
    return puzzleDepth4to20[depthIndex][puzzleIndex]

# Where the user can input their own puzzle and must do ctrl + z to exit
def userPuzzle() -> list:
    puzzle = []
    print("CTRL + Z to exit")
    while True:
        try:
            line = input().split()
            values = [int(x) for x in line]
        except EOFError:
            break
        puzzle.extend(values)
    return puzzle

# checking for invariants and ignoring 0 as it is the empty tile, returning true or false
def validity(puzzle : list[int]) -> bool:
    total = 0
    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if(puzzle[i] > puzzle[j] and puzzle[i] != 0 and puzzle[j] != 0):
                total += 1
    if total % 2 == 0:
        return True
    else:
        return False
    
# checking for misplaced tiles and retunring an integer
def h1(puzzle : list[int]) -> int:
    goalPuzzle = [0,1,2,3,4,5,6,7,8]
    misplacedTiles = 0
    for i in range(len(puzzle)):
        if puzzle[i] != goalPuzzle[i] and puzzle[i] != 0:
            misplacedTiles += 1
    return misplacedTiles

# returning the manhattan distance
def h2(puzzle: list[int]) -> int:
    goalPuzzle = [0,1,2,3,4,5,6,7,8]
    manhattanValue = 0

    for i in range(len(puzzle)):
        if puzzle[i] == 0:
            continue

        for j in range(len(goalPuzzle)):
            if puzzle[i] == goalPuzzle[j]:
                currentRow = i // 3
                currentCol = i % 3
                goalRow = j // 3
                goalCol = j % 3
                manhattanValue += (abs(currentRow - goalRow) + abs(currentCol - goalCol))
                break

    return manhattanValue

# returning a function when the user picks 
def pickHeuristic():
    heuristic = input("[h1] = # of misplaced tiles\n[h2] = sum of manhattan distances\n").upper()
    if heuristic == "H1":
        return h1
    elif heuristic == "H2":
        return h2
    else:
        print("Invalid input")

def printPuzzle(puzzle: list[int]):
    for i in range(0,3):
        print(f" {puzzle[i]} |", end="")
    print("\n------------")
    for i in range(3,6):
        print(f" {puzzle[i]} |", end="")
    print("\n------------")
    for i in range(6,9):
        print(f" {puzzle[i]} |", end="")
    print("\n------------")

#depending on the location of the index, it returns a list of actions
def actions(puzzle: list[int]):
    actionsList = []
    for i in range(len(puzzle)):
        if puzzle[i] == 0:
            currentRow = i // 3
            currentCol = i % 3
    if currentRow == 0:
        actionsList.append("Down")
    elif currentRow == 1:
            actionsList.append("Down")
            actionsList.append("Up")
    else:
        actionsList.append("Up")

    if currentCol == 0:
        actionsList.append("Right")
    elif currentCol == 1:
        actionsList.append("Right")
        actionsList.append("Left")
    else:
        actionsList.append("Left")

    return actionsList
# this will print from the root to the goal 
def pathFinder(goalNode):
    path = []
    current = goalNode
    while current != None:
        path.append(current)
        current = current.parent
    path.reverse() 
    step = 0
    for node in path:
        if node.action != None:
            step +=1
            print(f"Step: {step}\n")
        printPuzzle(node.state)

# this solves the puzzle by adding nodes to the frontier, and the explored set, returning the node
def solve(puzzle: list[int], heuristic):
    searchCost = 1
    goalPuzzle = [0,1,2,3,4,5,6,7,8]
    parent = Node(puzzle)
    frontier = PriorityQueue()
    frontier.put((0, parent))
    exploredSet = set()
    while not frontier.empty():
        node = frontier.get()[1]
        if node.state == goalPuzzle:
            return node, searchCost
        elif tuple(node.state) in exploredSet:
            continue
        else:
            exploredSet.add(tuple(node.state))
            actionsList = actions(node.state)
            for action in actionsList:
                child = node.childNode(action)
                searchCost += 1
                evaluationFunction = child.pathCost + heuristic(child.state)
                frontier.put((evaluationFunction, child))

# takes 100 puzzles, runs them on h1 and h2, prints their results to the terminal
def runTests():
    numberOfTests = 100
    puzzles = []
    results = {}

    for i in range(numberOfTests):
        puzzles.append(generatePuzzle())

    # Test h1
    for puzzle in puzzles:
        startTime = time.perf_counter()
        goalNode, searchCost = solve(puzzle, h1)
        totalTime = time.perf_counter() - startTime
        depth = goalNode.pathCost
        if depth not in results:
            results[depth] = {"puzzleCount": 0,"h1Time": 0,"h1SearchCost": 0,"h2Time": 0,"h2SearchCost": 0}

        results[depth]["puzzleCount"] += 1
        results[depth]["h1Time"] += totalTime
        results[depth]["h1SearchCost"] += searchCost

    # Test h2 using the same puzzles
    for puzzle in puzzles:
        startTime = time.perf_counter()
        goalNode, searchCost = solve(puzzle, h2)
        totalTime = time.perf_counter() - startTime
        depth = goalNode.pathCost

        results[depth]["h2Time"] += totalTime
        results[depth]["h2SearchCost"] += searchCost

    # printing the averages for each solution depth
    print(f"{'Depth':<8}", end="")
    print(f"{'Puzzles ':<8}", end="")
    print(f"{'h1 Nodes':<14}", end="")
    print(f"{'h2 Nodes':<14}", end="")
    print(f"{'h1 Time (s)':<15}", end="")
    print(f"{'h2 Time (s)':<15}")

    for depth in sorted(results):
        row = results[depth]
        puzzleCount = row["puzzleCount"]

        print(f"{depth:<8}", end="")
        print(f"{puzzleCount:<8}", end="")
        print(f"{row['h1SearchCost'] / puzzleCount:<14.0f}", end="")
        print(f"{row['h2SearchCost'] / puzzleCount:<14.0f}", end="")
        print(f"{row['h1Time'] / puzzleCount:<15.6f}", end="")
        print(f"{row['h2Time'] / puzzleCount:<15.6f}")

def main():
    choice = input("Enter A for a random 8-puzzle problem as input\nEnter B to enter your own specific 8-puzzle configuration\n").upper()
    if choice == "A":
        puzzle = generatePuzzle()
        printPuzzle(puzzle)
        heuristic = pickHeuristic()
        startTime = time.perf_counter()
        goalNode, searchCost= solve(puzzle,heuristic)
        totalTime = time.perf_counter() - startTime
        pathFinder(goalNode)
        print(f"Search Cost: {searchCost}\nTime : {totalTime:.6f}")
    elif choice == "B":
        puzzle = userPuzzle()
        printPuzzle(puzzle)
        if validity(puzzle) == False:
            print("The puzzle is invalid.")
        else:
            heuristic = pickHeuristic()
            startTime = time.perf_counter()
            goalNode, searchCost= solve(puzzle,heuristic)
            totalTime = time.perf_counter() - startTime
            pathFinder(goalNode)
            print(f"Search Cost: {searchCost}\nTime : {totalTime:.6f}")
    else:
        print("Invalid input")

    # running the test
    #runTests()
    
main()