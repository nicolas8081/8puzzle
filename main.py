import random
class Node:
    def __init__(self, state, parent=None, action=None, pathCost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.pathCost = pathCost

    def childNode(self, action):
        i = self.state.index(0)
        offsets = {"Up": -3, "Down": 3, "Left": -1, "Right": 1}
        j = i + offsets[action]
        newState = list(self.state)
        newState[i], newState[j] = newState[j], newState[i]

        return Node(newState, self, action, self.pathCost + 1)

def generatePuzzle():
    depthIndex = random.randint(0,4)
    puzzleIndex = random.randint(0,8)
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

def validity(puzzle : list[int]) -> bool:
    total = 0
    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if(puzzle[i] > puzzle[j] and puzzle[i] != 0 and puzzle[j] != 0):
                total += 1 
    print(total)
    if total % 2 == 0:
        return True
    else:
        return False

def h1(puzzle : list[int]) -> int:
    goalPuzzle = [0,1,2,3,4,5,6,7,8]
    misplacedTiles = 0
    for i in range(len(puzzle)):
        if puzzle[i] != goalPuzzle[i] and puzzle[i] != 0:
            misplacedTiles += 1
    return misplacedTiles

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
                manhattanValue += (abs(currentRow - goalRow)+ abs(currentCol - goalCol))
                break

    return manhattanValue

def pickHeuristic():
    heuristic = input("[h1] = # of misplaced tiles\n[h2] = sum of manhattan distances\n").upper()
    if heuristic == "H1":
        return heuristic
    elif heuristic == "H2":
        return heuristic
    else:
        print("Invalid input")

def printPuzzle(puzzle: list[int]) -> int:
    for i in range(0,3):
        print(f" {puzzle[i]} |", end="")
    print("\n------------")
    for i in range(3,6):
        print(f" {puzzle[i]} |", end="")
    print("\n------------")
    for i in range(6,9):
        print(f" {puzzle[i]} |", end="")
    print("\n------------")


    
def main():
    choice = input("Enter A for a random 8-puzzle problem as input\nEnter B to enter your own specific 8-puzzle configuration\n").upper()
    if choice == "A":
        puzzle = generatePuzzle()
        printPuzzle(puzzle)
        choice = pickHeuristic()
    elif choice == "B":
        puzzle = userPuzzle()
        printPuzzle(puzzle)
        if validity(puzzle) == False:
            print("The puzzle is invalid.")
        else:
            choice = pickHeuristic()
    else:
        print("Invalid input")
    
main()