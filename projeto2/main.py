from automata import *

def main():
    regex = input("\nDigite o regex: ")
    node = createAutomata(regex)
    print(node)


if __name__ == '__main__':
    main()

