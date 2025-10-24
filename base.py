import random

def random_vector(limit=10, length=3):
    return [random.randint(0, limit) for _ in range(length)]


class Vector:
    """
    A lightweight vector abstraction.
    Teaches: inner product logic, vector length handling, and abstraction boundaries.
    """
    def __init__(self, list_of_numbers=None):
        if list_of_numbers is None:
            self.vector = []
        elif list_of_numbers == "create":
            self.vector = random_vector()
            print("Initiating Normal vector with length : 3 and num-limmit:10")

        elif type(list_of_numbers) == Vector:
            self.vector = list_of_numbers  #FIX Made direct initialisation of vector to the matrix
        else:
            self.vector = list(list_of_numbers)  # make a safe copy

    def __str__(self):
        return str(self.vector)

    def add(self, number):
        self.vector.append(number)

    def __len__(self):
        return len(self.vector)

    def scaller_output(self, number):
        output_vector = Vector()
        for i in self.vector:
            output_vector.add(number * i)
        self.vector = output_vector


    def inner_product(self, other_vector):
        # Validation principle
        if len(self.vector) != len(other_vector.vector):
            raise ValueError("Incompatible vectors for inner product")

        product = sum(a * b for a, b in zip(self.vector, other_vector.vector))
        print(f"Inner product of {self.vector} and {other_vector.vector} = {product}")
        return product

    def transpose(self):
        return [[x] for x in self.vector]  # column representation


class Matrix:
    """
    Matrix abstraction to teach:
    - Shape inference
    - Row-column operations
    - Matrix multiplication as composition of inner products
    """
    def __init__(self, rows=None):
        if rows == None:
            self.rows = []
            self.columns = []
            self.shape = (0,0) # Make it an function to call)

        # TODO Required Matrix based initialisatioin tool and colum init function 
        elif type(rows) == Matrix:  # Adding slef initialisation tool
            self.rows = rows.rows 
            self.columns = rows.columns
            self.shape = rows.shape

        elif not all(len(row) == len(rows[0]) for row in rows):
            raise ValueError("Inconsistent row lengths")

        else:
            self.rows = [Vector(row) for row in rows]
            self.columns = [Vector([row.vector[i] for row in self.rows]) for i in range(len(rows[0]))]
            self.shape = (len(self.rows), len(self.columns))

    def __str__(self):
        return "\n".join(str(row.vector) for row in self.rows)

    def add(self, vector_element):
        #BUG Validation is requried here 
        if type(vector_element) == Vector():
            self.rows.append(vector_element)
            # Initialise base collum list to addup
            self.columns = []
            for element in vector_element.vector:
                self.columns.append([[element]])
             
        else:
            print(f"Non vector entity is been detected : {vector_element}")
            self.rows.append(Vector(vector_element))
            for element in vector_element.vector:
                self.columns.append([[element]])

    def multiply_scaller(self, number):
        output = Matrix()
        for row in self.rows:
            scaller_vector = row.scaller_output(number)
            output.add(scaller_vector)

        self.rows = output  #  Error prone step Matrix object isnt organised for Vector Abstraction 

    
    def multiply(self, other):
        # Dimension principle
        if self.shape[1] != other.shape[0]:
            raise ValueError("Shape mismatch for matrix multiplication")

        result = []
        for row in self.rows:
            result_row = []
            for col in other.columns:
                result_row.append(row.inner_product(col))
            result.append(result_row)

        return Matrix(result)
