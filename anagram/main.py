words = [ 'a', 'other', 'bat', 'cat', 'cta', 'tab']
anagrams = {}


def organise(word):
    sorted_word = ''.join(sorted(word))
    if sorted_word in anagrams.keys():
        anagrams[sorted_word].append(word)
    else:
        anagrams[sorted_word] = [word]


for word in words:
    organise(word)

print(f'{list(anagrams.values())}')
