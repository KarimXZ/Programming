import random as rd;
class Matrix():
    def __init__(self, row, column):
        self.__row=row
        self.__column=column
        self.matrix =[[rd.randint(0,10) for j in range(row)] for i in range(column)]
    def updatevalue(self,row,column,newvalue):
        self.matrix[row[column]]=newvalue
    def getvalue(self,row,column):
        return self.matrix[row[column]];
    def getrow(self,row):
        return self.matrix[row]
    def getcolumn(self,column):
        for i in self.matrix:
            return i[column]
    def printmatrix(self):
        for i in self.matrix:
            print(i)
    @staticmethod
    def addMatrix(A,B):
        if len(A.matrix)==len(B.matrix) and len(A.matrix[0])==len(B.matrix[0]):
            newmatrix=ZeroMatrix(len(A.matrix), len(A.matrix[0]))
            for i in range(len(A.matrix)):
                for j in range(len(A.matrix[0])):
                    newmatrix.matrix[i][j]=A.matrix[i][j]+B.matrix[i][j]
            for i in newmatrix.matrix:
                print(i)
        else:
            print("Matrislerin boyutu yanlistir")
    def createObjectMatrix(cls,A):
        ObjectMatrix=Matrix(0,1)
        for i in A.matrix:
            for j in i:
                ObjectMatrix.matrix.append(j)
        return ObjectMatrix.matrix

class ZeroMatrix(Matrix):
    def __init(self,row,column):
        super().__init__(row,column)
        self.matrix =[[rd.randint(0,0) for j in range(row)] for i in range(column)]

A=Matrix(3,3)
B=Matrix(3,3)
A.printmatrix()
B.printmatrix()
Matrix.addMatrix(A, B)
print(Matrix.createObjectMatrix(Matrix,A))
