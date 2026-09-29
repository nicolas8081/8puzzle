import sys
def generatePuzzle():
    ...

def userPuzzle():
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

def main():
    choice = input("Enter A for a random 8-puzzle problem as input\nEnter B to enter your own specific 8-puzzle configuration\n").upper()
    if choice == "A":
        generatePuzzle()
    elif choice == "B":
        puzzle = userPuzzle()
        print(puzzle)
    else:
        print("Invalid input")
    
main()