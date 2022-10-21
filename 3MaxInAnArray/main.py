"""
Return max 3 numbers in input array sorted in ascending order with using sort
"""

RESULT = [None, None, None]

def three_max_in_array_in_order(input_array):
    for number in input_array:
        update_result(number)

def update_result(number):
    if RESULT[2] is None or number > RESULT[2]:
        shift_and_update(number, 2)
    elif RESULT[1] is None or number > RESULT[1]:
        shift_and_update(number, 1)
    elif RESULT[0] is None or number > RESULT[0]:
        shift_and_update(number, 0)

def shift_and_update(number, idx):
    for i in range(idx + 1):
        if i == idx:
            RESULT[i] = number
        else:
            RESULT[i] = RESULT[i + 1]

three_max_in_array_in_order([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7])
print(RESULT)
