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
        m = []
        if self.shape(rows):
            for row in rows:
                v = Vector(row)
                self.append(v)
        else:
            print("Matrix cant be initiated with given input")
        

    def __str__(self):
        return "\n".join(str(row) for row in self)

    def shape(self, matrix=None):
        if matrix == None:
            matrix = self
        n = len(matrix)
        check = 1
        m = len(matrix[0])
        for row in matrix[1:]:
            if len(row) != m:
                check *= 0
        if check:
            shape = (n, m)
            return shape
        else:
            print("Matrix is not valid and contains unambeguis things")
            return None
            
            

    def scale_with(self, number):
        scalled = []
        for row in self:
            row.scale_with(number)
            scalled.append(row)
        self.clear()
        self.extend(scalled)

    def transpose(self):
        """
            Legendary DSA question is to find the transpose without making copy of matrix
        """
        if len(self) == len(self[0]):
            pass

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

