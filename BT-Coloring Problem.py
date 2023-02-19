import numpy as np


class Region:
    def __init__(self, degree, color):
        # The degree of region
        self.degree = degree
        # Region is not colored
        self.color = -1
        # Neighbour of region
        self.neighbourRegion = []
        # The number of possible color
        self.number_of_PossibleColor = len(colors)
        self.possibleColors = [True] * self.number_of_PossibleColor
        self.changed = []

    def setColor(self, color):
        # Region can't be colored
        if self.possibleColors[color] == False:
            return False

        self.color = color
        for i in self.neighbourRegion:
            if i not in visitedRegion:
                if listofRegion[i].possibleColors[color] == True:
                    listofRegion[i].possibleColors[color] = False
                    listofRegion[i].number_of_PossibleColor -= 1
                    self.changed.append(i)
        return True

    def restore(self, color):
        for i in self.changed:
            listofRegion[i].possibleColors[color] = True
            listofRegion[i].number_of_PossibleColor += 1
        self.changed.clear()
        self.color = -1

    def addNeibourRegion(self, l):
        self.neighbourRegion.append(l)

    def __lt__(self, other):
        if self.number_of_PossibleColor > other.number_of_PossibleColor:
            return True
        elif self.number_of_PossibleColor == other.number_of_PossibleColor:
            if self.degree < other.degree:
                return True
        return False


def setRegion():
    length = len(matrix)
    for i in range(length):
        listofRegion.append(Region(np.sum(matrix[i]), colors))
        for j in range(length):
            if matrix[i][j] == 1:
                listofRegion[i].addNeibourRegion(j)


def checkcontraint(x, color):
    for i in listofRegion[x].neighbourRegion:
        if color == listofRegion[i].color:
            return False
    return True


def findNextRegion():
    flag = True
    nextRegion = -1
    for x in range(len(listofRegion)):
        if x not in visitedRegion:
            if flag:
                nextRegion = x
                flag = False
            else:
                if listofRegion[nextRegion] < listofRegion[x]:
                    nextRegion = x
    return nextRegion


def mrv(x):
    flag = True
    if x == -1:
        # print("------------------------------------")
        for i in range(len(listofRegion)):
            print("Vertex {} has color {}".format(i, colors[listofRegion[i].color]))
            ans.append(listofRegion[i].color)
        return True
    for color in range(len(colors)):
        if checkcontraint(x, color):
            if listofRegion[x].setColor(color):
                print ('Vertex {} -> {}'.format(x, colors[color]))
                flag = False
                visitedRegion.add(x)
                y = findNextRegion()
                if mrv(y):
                    return True
                visitedRegion.remove(x)
                listofRegion[x].restore(color)
        # if flag:
          # print('Vertex {} -> No suitable color'.format(x))
    return False


def backtrack(_matrix, _colors):
    global matrix
    global colors
    global listofRegion
    global visitedRegion
    global ans

    matrix = _matrix
    colors = _colors
    listofRegion = []
    visitedRegion = set()
    ans = []
    setRegion()
    x = findNextRegion()
    if mrv(x) == False:
        return [0] * len(matrix)
    return ans

        #  0  1  2  3  4  5  6
matrix = [[0, 1, 1, 1, 1, 1, 0], # 0
          [1, 0, 1, 0, 0, 0, 0], # 1
          [1, 1, 0, 1, 0, 0, 0], # 2
          [1, 0, 1, 0, 1, 0, 0], # 3
          [1, 0, 0, 1, 0, 1, 0], # 4
          [1, 0, 0, 0, 1, 0, 0], # 5
          [0, 0, 0, 0, 0, 0, 0]] # 6

colors = ['red','blue','green']

if __name__ == '__main__':
    backtrack(matrix, colors)