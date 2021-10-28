# Given a string, return the count of the number of times that a substring length 2 appears in the string
# and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
    #when you count, open an empty string first
    count = 0
    if len(str) <= 2:
        return 0

    for i in range(len(str)-2): #when you wanna go through each char in string, open for loop
                                #range(len()): In string/list, use this in a for loop to access by Inex
        if str[i:i+2] == str[len(str)-2:]:
            count += 1

    return count

print(last2('xxaxxaxxaxx'))