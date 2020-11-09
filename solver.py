#!/usr/bin/python3
board = [
[1  , 1, "u","u"],
["u","u","u","u"],
["u","u","u","u"]
]
possibilities = set()
poses = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for i in range(len(board)):
	for j in range(len(board[i])):
		tile = board[i][j]
		if not (tile == "u" or tile == "m" or tile == 0):
			for pos in poses:
				if (not (i+pos[0] < 0 or j+pos[1] < 0)) and board[i+pos[0]][j+pos[1]] == "u":
					possibilities.add((i+pos[0], j+pos[1]))
print(possibilities)

			