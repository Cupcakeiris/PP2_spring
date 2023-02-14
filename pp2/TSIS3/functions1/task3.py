def solve(numheads, numlegs):
    row1 = [1, 1]
    row2 = [2, 4]
    b = [numheads, numlegs]
    """
        1 1 | 35
        2 4 | 94
    """

    #RREF
    row2 = [row2[0] - 2*row1[0], row2[1] - 2*row1[1]]
    b = [numheads, b[1] - 2*b[0]]
    """
        1 1 | 35
        0 2 | 24
    """

    row2 = [row2[0]/2, row2[1]/2]
    b = [numheads, b[1]/2]
    """
        1 1 | 35
        0 1 | 12
    """

    row1 = [row1[0], row1[1] - row2[1]]
    b = [b[0] - b[1], b[1]]
    """
        1 0 | 23
        0 1 | 12
    """
    matrix = [row1, row2, b]
    chicken = int(matrix[2][0])
    rabbit = int(matrix[2][1])

    print("Chicken:", chicken, "Rabbit:", rabbit)

h = int(input("Heads: "))
l = int(input("Legs: "))  
solve(h, l)