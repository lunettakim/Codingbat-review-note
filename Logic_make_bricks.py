# We want to make a row of bricks that is goal inches long.
# We have a number of small bricks (1 inch each) and big bricks (5 inches each).
# Return True if it is possible to make the goal by choosing from the given bricks.
# make_bricks(3, 1, 8) → True

def make_bricks(small,big,goal):
    #Think about 'False' cases -- 1) when goal is bigger than the sum of small+big*5
    # 2) when small blocks are not enough after using big blocks

    if (goal > small + big*5) or (goal%5 > small):
        return False
    return True



