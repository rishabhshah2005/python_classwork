# WAP that add and subtract given matrix object
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
    
# https://circuitverse.org/users/77435/projects/chess-clock-6367e23f-07b6-4102-b0a5-6d4c460656d2