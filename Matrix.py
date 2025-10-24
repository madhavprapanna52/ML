"""
    Matrix
    An one level abstraction of vectors Featuring vectors bundles and tranformative linear functions
    Serving transformations via defined numbers and computations
    handeling vectors combinations
"""
from Vector import *


class Matrix(list):
    """
    Matrix Abstraction on top of vector element
    Functionality 
        1. Representing transformation
        2. Abstraction of computations for solving equation
        3. Handeling fiting and equations abstractions for ML
    """

    def __init__(self, rows=None):
        if type(rows) == list:
            for row in rows:
                v = Vector(row)
                self.append(v)

    def __str__(self):
        return "\n".join(str(row) for row in self)

    def colums(self):
        columns = []
        # Initialize collums via doubel iteration
        iter_column = 0
        
        while iter_column < len(self[0]):
            column_element = []
            for row in self:
                column_element.append(row[iter_column])
            iter_column += 1
            columns.append(column_element)

        return Matrix(columns)

l = [[1,2] , [3,4]]
m = Matrix(l)
print(f"matrix check")
print(m)
print(f"Matrix columns")
print(m.colums())

