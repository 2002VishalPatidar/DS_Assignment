def first_non_repeated_char(str):
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in str:
        if char_count[char] == 1:
            return char
    return None
str= "vishal"
print(first_non_repeated_char(str))
string="aankit"
print(first_non_repeated_char(string))