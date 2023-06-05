#!/usr/bin/python3
"""module to solve nqueens puzzle"""


import sys


def solve_nqueens():
    """finds every possible solution to the puzzle

    Returns:
        list of possible solutions

    """

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    main = []
    p_sol = N - 2
    for i in range(p_sol):
        main.append([])
    j = 0
    while j < N:
        sol = []
        sol.append(j)
        p = 0
        k = 0
        while k < N:
            if j != k and k != abs(j - (N - 1)):
                sol.append(k)
                main[p].append(sol.copy())
                p += 1
                sol.pop()
            k += 1
        j += 1
    return main


if __name__ == "__main__":
    queens = solve_nqueens()
    for i in queens:
        print(i)
