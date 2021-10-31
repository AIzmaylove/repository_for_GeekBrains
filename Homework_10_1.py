class Matrix:
    def __init__(self, list_1, list_2):

        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        zero_matrix = [[0,0,0],
                       [0,0,0],
                       [0,0,0]]

        for i in range(len(self.list_1)):
            for j in range(len(self.list_2)):
                zero_matrix[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in zero_matrix]))

    
my_matrix = Matrix([[5, 8, 10],
                    [1, 1, 1],
                    [1, 1, 1]],
                   [[1, 8, 3],
                    [1, 1, 1],
                    [1, 5, 97]])

print(my_matrix.__add__())