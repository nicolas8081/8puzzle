def generatePuzzle():
    puzzleDepth4 = [
    [1, 2, 5, 3, 4, 8, 6, 7, 0],
    [1, 2, 5, 3, 0, 4, 6, 7, 8],
    [1, 4, 2, 6, 3, 5, 0, 7, 8],
    [1, 4, 0, 3, 5, 2, 6, 7, 8],
    [1, 4, 2, 3, 5, 8, 6, 7, 0],
    [1, 4, 2, 3, 7, 5, 0, 6, 8],
    [1, 4, 2, 3, 7, 5, 6, 8, 0],
    [0, 3, 2, 4, 1, 5, 6, 7, 8],
    [3, 2, 0, 4, 1, 5, 6, 7, 8],
    [3, 1, 0, 4, 5, 2, 6, 7, 8],
    ]

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
def main():
    choice = input("Enter A for a random 8-puzzle problem as input\nEnter B to enter your own specific 8-puzzle configuration\n").upper()
    if choice == "A":
        generatePuzzle()
    elif choice == "B":
        puzzle = userPuzzle()
        print(puzzle)
    else:
        print("Invalid input")
    
    if validity(puzzle) == False:
        print("The puzzle is invalid.")
    else: 
        heuristic = input("[h1] = # of misplaced tiles\n[h2] = sum of manhattan distances\n")
        print(h1([3, 1, 0, 4, 5, 2, 6, 7, 8]))
        print(h2([3, 1, 0, 4, 5, 2, 6, 7, 8]))
        
main()