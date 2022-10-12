def first_non_repeating_character_index(input_text):
    chars_count = {}
    for each_char in input_text:
        chars_count[each_char] = chars_count.get(each_char, 0) + 1
    for idx, character in enumerate(input_text):
        if chars_count[character] == 1:
            return idx
    return -1



print(first_non_repeating_character_index('abbcdcaf'))
