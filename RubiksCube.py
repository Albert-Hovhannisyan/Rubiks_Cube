import numpy as np

class Front:
    def __init__(self):
        self.arr = np.array([
            ["R1", "R2", "R3"],
            ["R4", "R5", "R6"],
            ["R7", "R8", "R9"]])
    
    def get_front(self):
        return self.arr
      
    def set_front(self, x):
        self.arr = x

class Back:
    def __init__(self):
        self.arr = np.array([
            ["O1", "O2", "O3"],
            ["O4", "O5", "O6"],
            ["O7", "O8", "O9"]])
    
    def get_back(self):
        return self.arr
      
    def set_back(self, x):
        self.arr = x
    
class Top:
    def __init__(self):
        self.arr = np.array([
            ["Y1", "Y2", "Y3"],
            ["Y4", "Y5", "Y6"],
            ["Y7", "Y8", "Y9"]])
    
    def get_top(self):
        return self.arr
      
    def set_top(self, x):
        self.arr = x

class Bottom:
    def __init__(self):
        self.arr = np.array([
            ["W1", "W2", "W3"],
            ["W4", "W5", "W6"],
            ["W7", "W8", "W9"]])
    
    def get_bottom(self):
        return self.arr
      
    def set_bottom(self, x):
        self.arr = x

class Right:
    def __init__(self):
        self.arr = np.array([
            ["G1", "G2", "G3"],
            ["G4", "G5", "G6"],
            ["G7", "G8", "G9"]])
    
    def get_right(self):
        return self.arr
      
    def set_right(self, x):
        self.arr = x

class Left:
    def __init__(self):
        self.arr = np.array([
            ["B1", "B2", "B3"],
            ["B4", "B5", "B6"],
            ["B7", "B8", "B9"]])
    
    def get_left(self):
        return self.arr
      
    def set_left(self, x):
        self.arr = x

# front = np.array([
#     ["R1", "R2", "R3"],
#     ["R4", "R5", "R6"],
#     ["R7", "R8", "R9"]])

# back = np.array([
#     ["O1", "O2", "O3"],
#     ["O4", "O5", "O6"],
#     ["O7", "O8", "O9"]])

# top = np.array([
#     ["Y1", "Y2", "Y3"],
#     ["Y4", "Y5", "Y6"],
#     ["Y7", "Y8", "Y9"]])

# bottom = np.array([
#     ["W1", "W2", "W3"],
#     ["W4", "W5", "W6"],
#     ["W7", "W8", "W9"]])

# right = np.array([
#     ["G1", "G2", "G3"],
#     ["G4", "G5", "G6"],
#     ["G7", "G8", "G9"]])

# left = np.array([
#     ["B1", "B2", "B3"],
#     ["B4", "B5", "B6"],
#     ["B7", "B8", "B9"]])

# Experiments

def rotate(face, x):
    return np.rot90(face, x)

def swapfaces(a, b, c, d, n):
    tmp = [0, 0, 0]
    for i in range(3):
        tmp[i] = a[n][i]
    for i in range(3):
        a[n][n-i] = b[i][n]
    for i in range(3):
        b[i][n] = c[0][i]
    for i in range(3):
        c[0][i] = d[n-i][0]
    for i in range(3):
        d[i][0] = tmp[i]
    return [a, b, c, d]

# def swapfaces(a, b, c, d, n):
#     tmp = [a[2][0], a[2][1], a[2][2]]
#     for i in range(3):
#         a[n][n-i] = b[i][n]
#         b[i][n] = c[0][i]
#         c[0][i] = d[n-i][0]
#         d[i][0] = tmp[i]
#     return [a, b, c, d]

front = Front()
back = Back()
top = Top()
bottom = Bottom()
right = Right()
left = Left()

def F():
    tmp = rotate(front.get_front(), -1)
    front.set_front(tmp)
    tmp = swapfaces(top.get_top(), left.get_left(), bottom.get_bottom(), right.get_right(), 2)
    top.set_top(tmp[0])
    left.set_left(tmp[1])
    bottom.set_bottom(tmp[2])
    right.set_right(tmp[3])
    # tmp = swapfaces(top.get_top(), left.get_left(), bottom.get_bottom(), right.get_right(), 2)
    # top.set_top(tmp[0])
    # left.set_left(tmp[1])
    # bottom.set_bottom(tmp[2])
    # right.set_right(tmp[3])
    print(front.get_front())
    print(top.get_top())
    print(left.get_left())
    print(bottom.get_bottom())
    print(right.get_right())

# def F2():
#     tmp = rotate(front.get_front(), 2)
#     front.set_front(tmp)

# def F_Prime():
#     tmp = rotate(front.get_front(), -1)
#     front.set_front(tmp)
    
F()
#print(front.get_front())