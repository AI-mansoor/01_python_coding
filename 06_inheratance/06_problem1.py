class twoD:
    def __init__(self,i,j):
        self.i = i
        self.j = j

def show(self):
    print(f"The 2d vector is {self.i}i + {self.j}j")


class threeD(twoD):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k


def show(self):
    print(f"The 3d vector is {self.i}i + {self.j}j + {self.k}k")

a = twoD(2,3)
a.show()

b = threeD(2,3,4)
b.show()