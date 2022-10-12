WORDS = [ 'a', 'other', 'bat', 'cat', 'cta', 'tab']
ANAGRAMS = {}


def organize(input_word):
    sorted_word = ''.join(sorted(input_word))
    if sorted_word in ANAGRAMS.keys():
        ANAGRAMS[sorted_word].append(input_word)
    else:
        ANAGRAMS[sorted_word] = [input_word]


for word in WORDS:
    organize(word)

print(f'{list(ANAGRAMS.values())}')
