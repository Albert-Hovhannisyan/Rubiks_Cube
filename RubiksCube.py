import numpy as np

from Cube import Cube

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
    
class Up:
    def __init__(self):
        self.arr = np.array([
            ["Y1", "Y2", "Y3"],
            ["Y4", "Y5", "Y6"],
            ["Y7", "Y8", "Y9"]])
    
    def get_up(self):
        return self.arr
      
    def set_up(self, x):
        self.arr = x

class Down:
    def __init__(self):
        self.arr = np.array([
            ["W1", "W2", "W3"],
            ["W4", "W5", "W6"],
            ["W7", "W8", "W9"]])
    
    def get_down(self):
        return self.arr
      
    def set_down(self, x):
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

# def swapfaces(a, b, c, d, n):
#     tmp = [0, 0, 0]
#     for i in range(3):
#         tmp[i] = a[n][i]
#     for i in range(3):
#         a[n][n-i] = b[i][n]
#     for i in range(3):
#         b[i][n] = c[0][i]
#     for i in range(3):
#         c[0][i] = d[n-i][0]
#     for i in range(3):
#         d[i][0] = tmp[i]
#     return [a, b, c, d]

def swapfacesFront(up, left, down, right, n):

    for j in range(n):
        tmp = [up[2][0], up[2][1], up[2][2]]

        up[2][0] = left[2][2]
        up[2][1] = left[1][2]
        up[2][2] = left[0][2]

        left[0][2] = down[0][0]
        left[1][2] = down[0][1]
        left[2][2] = down[0][2]

        down[0][0] = right[2][0]
        down[0][1] = right[1][0]
        down[0][2] = right[0][0]

        right[0][0] = tmp[0]
        right[1][0] = tmp[1]
        right[2][0] = tmp[2]

    return [up, left, down, right]

def swapfacesBack(up, right, down, left, n):

    for j in range(n):
        tmp = [up[0][0], up[0][1], up[0][2]]

        up[0][0] = right[0][2]
        up[0][1] = right[1][2]
        up[0][2] = right[2][2]

        right[0][2] = down[2][2]
        right[1][2] = down[2][1]
        right[2][2] = down[2][0]

        down[2][0] = left[0][0]
        down[2][1] = left[1][0]
        down[2][2] = left[2][0]

        left[0][0] = tmp[2]
        left[1][0] = tmp[1]
        left[2][0] = tmp[0]

    return [up, right, down, left]

def swapfacesUp(front, right, back, left, n):
    for j in range(n):
        tmp = [front[0][0], front[0][1], front[0][2]]

        front[0][0] = right[0][0]
        front[0][1] = right[0][1]
        front[0][2] = right[0][2]

        right[0][0] = back[0][0]
        right[0][1] = back[0][1]
        right[0][2] = back[0][2]

        back[0][0] = left[0][0]
        back[0][1] = left[0][1]
        back[0][2] = left[0][2]

        left[0][0] = tmp[0]
        left[0][1] = tmp[1]
        left[0][2] = tmp[2]

    return [front, right, back, left]

def swapfacesDown(front, left, back, right, n):
    for j in range(n):
        tmp = [front[2][0], front[2][1], front[2][2]]

        front[2][0] = left[2][0]
        front[2][1] = left[2][1]
        front[2][2] = left[2][2]

        left[2][0] = back[2][0]
        left[2][1] = back[2][1]
        left[2][2] = back[2][2]

        back[2][0] = right[2][0]
        back[2][1] = right[2][1]
        back[2][2] = right[2][2]

        right[2][0] = tmp[0]
        right[2][1] = tmp[1]
        right[2][2] = tmp[2]

    return [front, left, back, right]

def swapfacesLeft(up, back, down, front, n):
    for j in range(n):
        tmp = [up[0][0], up[1][0], up[2][0]]

        up[0][0] = back[2][2]
        up[1][0] = back[1][2]
        up[2][0] = back[0][2]

        back[0][2] = down[2][0]
        back[1][2] = down[1][0]
        back[2][2] = down[0][0]

        down[0][0] = front[0][0]
        down[1][0] = front[1][0]
        down[2][0] = front[2][0]

        front[0][0] = tmp[0]
        front[1][0] = tmp[1]
        front[2][0] = tmp[2]

    return [up, back, down, front]

def swapfacesRight(up, front, down, back, n):
    for j in range(n):
        tmp = [up[0][2], up[1][2], up[2][2]]

        up[0][2] = front[0][2]
        up[1][2] = front[1][2]
        up[2][2] = front[2][2]

        front[0][2] = down[0][2]
        front[1][2] = down[1][2]
        front[2][2] = down[2][2]

        down[0][2] = back[2][0]
        down[1][2] = back[1][0]
        down[2][2] = back[0][0]

        back[0][0] = tmp[2]
        back[1][0] = tmp[1]
        back[2][0] = tmp[0]

    return [up, front, down, back]

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
up = Up()
down = Down()
left = Left()
right = Right()

def F():
    tmp = rotate(front.get_front(), -1)
    front.set_front(tmp)
    tmp = swapfacesFront(up.get_up(), left.get_left(), down.get_down(), right.get_right(), 1)
    up.set_up(tmp[0])
    left.set_left(tmp[1])
    down.set_down(tmp[2])
    right.set_right(tmp[3])
    print(front.get_front())
    print(up.get_up())
    print(left.get_left())
    print(down.get_down())
    print(right.get_right())

def B():
    tmp = rotate(back.get_back(), -1)
    back.set_back(tmp)
    tmp = swapfacesBack(up.get_up(), right.get_right(), down.get_down(), left.get_left(), 1)
    up.set_up(tmp[0])
    right.set_right(tmp[1])
    down.set_down(tmp[2])
    left.set_left(tmp[3])
    print(back.get_back())
    print(up.get_up())
    print(right.get_right())
    print(down.get_down())
    print(left.get_left())

def L():
    tmp = rotate(left.get_left(), -1)
    left.set_left(tmp)
    tmp = swapfacesLeft(up.get_up(), back.get_back(), down.get_down(), front.get_front(), 1)
    up.set_up(tmp[0])
    back.set_back(tmp[1])
    down.set_down(tmp[2])
    front.set_front(tmp[3])
    print(left.get_left())
    print(up.get_up())
    print(back.get_back())
    print(down.get_down())
    print(front.get_front())

def R():
    tmp = rotate(right.get_right(), -1)
    right.set_right(tmp)
    tmp = swapfacesRight(up.get_up(), front.get_front(), down.get_down(), back.get_back(), 1)
    up.set_up(tmp[0])
    front.set_front(tmp[1])
    down.set_down(tmp[2])
    back.set_back(tmp[3])
    print(right.get_right())
    print(up.get_up())
    print(front.get_front())
    print(down.get_down())
    print(back.get_back())

def U():
    tmp = rotate(up.get_up(), -1)
    up.set_up(tmp)
    tmp = swapfacesUp(front.get_front(), right.get_right(), back.get_back(), left.get_left(), 1)
    front.set_front(tmp[0])
    right.set_right(tmp[1])
    back.set_back(tmp[2])
    left.set_left(tmp[3])
    print(up.get_up())
    print(front.get_front())
    print(right.get_right())
    print(back.get_back())
    print(left.get_left())

def D():
    tmp = rotate(down.get_down(), -1)
    down.set_down(tmp)
    tmp = swapfacesDown(front.get_front(), left.get_left(), back.get_back(), right.get_right(), 1)
    front.set_front(tmp[0])
    left.set_left(tmp[1])
    back.set_back(tmp[2])
    right.set_right(tmp[3])
    print(down.get_down())
    print(front.get_front())
    print(left.get_left())
    print(back.get_back())
    print(right.get_right())
    
# F()
# L()
# R()
# D()
# U()
# B()

a = Cube()