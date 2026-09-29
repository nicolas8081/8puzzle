import sys

def main():
    choice = input("Enter A for a random 8-puzzle problem as input\nEnter B to enter your own specific 8-puzzle configuration\n")
    if choice == "B":
        lines = []
        while True:
            try:
                line = input().split()
                values = [int(x) for x in line]
                print(line)
            except EOFError:
                break
            lines.extend(values)
    print(lines)
main()