from automata import Automata

def main():
    regex = input("\nInput regex expression: ")
    automata = Automata()
    automata.createAutomata(regex)
    automata.print()
    automata.plot()


if __name__ == '__main__':
    main()

