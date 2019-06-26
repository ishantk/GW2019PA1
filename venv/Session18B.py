# n-Queen Problem :)
# 1. Create a Chessboard of 8 X 8 with 1s and 0s
"""
1   0   1   0   1   0   1   0
0   9   0   1   0   1   0   1
1   0   1   9   1   0   1   0
0   1   0   1   0   1   0   1
1   0   1   0   1   0   1   0
0   1   0   1   9   1   0   1
1   0   1   0   1   0   1   0
0   1   0   1   0   1   0   9

"""

import numpy as np
import datetime as dt

stamp1 = dt.datetime.today()
chessBoard = np.zeros((8, 8), dtype=int)

# print(chessBoard)
#
# print()

# Slicing and Substitution
chessBoard[1::2, ::2] = 1
chessBoard[::2, 1::2] = 1

stamp2 = dt.datetime.today()
print("Time Taken to Create ChessBoard: ",stamp2-stamp1)

print(chessBoard)

# 2. Ask User to place 4 queens on chessboard
# Where to place 1st Queen : 2,3
# Where to place 2nd Queen : 5,4
# Where to place 3rd Queen : 1,1
# Where to place 4th Queen : 7,7
# and substitute 9 over thr

indexes = []

print()
for i in range(0,4):
    queenPosition = input("Where to place Queen #{} : ".format(i))
    i = int(queenPosition[0])
    j = int(queenPosition[2])

    if i not in indexes and j not in indexes:
        chessBoard[i][j] = 9
        indexes.append(i)
        indexes.append(j)
    else:
        print("Queen Exists. Enter Another Position")

    # PS: This above is a hint. :)

print(chessBoard)

# 3. Validate if a queen is available in the same row or same column
# give a message to the user to enter some other position


# 4. Validate if a queen is available in the same diagonal(s)
# give a message to the user to enter some other position
