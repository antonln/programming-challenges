def make_chocolate(small, big, goal):
    '''We want to make a package of goal kilos of chocolate. We have 
    small bars (1 kilo each) and big bars (5 kilos each). Return the 
    number of small bars to use, assuming we always use big bars 
    before small bars. Return -1 if not possible.'''
    
    small_wt = small * 1
    big_wt = big * 5

    if (small_wt + big_wt) < goal:
        return print("Not enough bars.")

    if big_wt >= goal:
        excess_wt = goal % 5
        big_used = (goal - excess_wt) / 5

    if big_wt < goal:
        excess_wt = goal - big_wt
        big_used = big

    if small_wt >= excess_wt:
        small_used = int(excess_wt / 1)     
        print("Big bars used: ", big_used)
        print("Small bars used: ", small_used)

    if small_wt < excess_wt:
        return print("Not enough small bars.")

goal = int(input("Enter goal: "))
big = int(input("Enter number of big bars: "))
small = int(input("Enter number of small bars: "))

make_chocolate(small,big,goal)
