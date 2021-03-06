from src.puzzle import Puzzle
from src.solver import Solver


def main():
    test_names = ["5by5",
                  "10by10",
                  "15by15",
                  "20by20",
                  "25by25",
                  "30by25",
                  "50by50"
                  ]
    tests = [] * len(test_names)
    for i in range(len(tests)):
        name = test_names[i]
        tests[i] = Solver(Puzzle(name,
                                 "lib\\" + name + "RowClues.txt",
                                 "lib\\" + name + "ColClues.txt"
                                 ))
        tests[i].priority_solve(update_solve=True)


if __name__ == "__main__":
    main()
