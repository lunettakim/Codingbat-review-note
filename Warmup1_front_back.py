# Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
    if len(str) <= 1:
        return str

    return str[-1] + str[1:-1] + str[0]

#first character : string[0]
#last character : string[-1] or str[len(str)-1]


print(front_back('Chocolate'))
