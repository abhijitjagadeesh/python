'''
Dynamically generate pattern like [[0, 0, 0], [0, 0, 0]]
'''

NUM_OF_ROWS = 2
NUM_OF_COLS = 3

# GRID = []
# for _ in range(NUM_OF_ROWS):
#     column = []
#     for _ in range(NUM_OF_COLS):
#         column.append(0)
#     GRID.append(column)

# print(GRID)

# same as above but using list comprehension
print([[0 for _ in range(NUM_OF_COLS)] for _ in range(NUM_OF_ROWS)])
