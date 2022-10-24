'''
Fizbuzz
'''

INPUT_ARRAY = [45, 22, 14, 65, 97, 72]

for idx, number in enumerate(INPUT_ARRAY):
    result = ''
    if number % 3 == 0:
        result = 'fizz'
    if number % 5 == 0:
        result += 'buzz'
    if result:
        INPUT_ARRAY[idx] = result

print(INPUT_ARRAY)
