# Function to find which level in a list an integer belongs to
# ex. levels = [2,4,6,8]
# 1 should return 0
# 2 should return 1
# 5 should return 2
def find_level(levels : list[int], n : int) :
    p = 0
    if n >= levels[len(levels)-1] :
        return len(levels)
    while (n >= levels[p]) :
        p += 1

    return p