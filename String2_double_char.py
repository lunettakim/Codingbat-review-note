# Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
    new_str = ''
    for i in str: #since you need each value not index, no need to write range(len(str))
        new_str += i*2

    return new_str

print(double_char('Hello-guys'))