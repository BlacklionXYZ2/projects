from math import prod
class matrix:
    def __init__(self, shape: tuple = None, data = None):
        # layer = self.__makelist(shape[-1])
        # for x in range(len(shape) - 1, 0, -1):
        #     layer = self.__makelist(shape[x - 1], layer)
        # self.mat = layer
        self.stride = shape
        self.mat = [0 for _ in range(prod(self.stride))]

    def __makelist(self, size, data = None): # deprecated in favour of strides
        return [data for _ in range(size)]
    
    def __combine_dim(self, stride, data = None):
        segments = []
        prev_x = 0
        for x in range(stride, len(data) + 1, stride):
            segments.append(data[prev_x:x])
            prev_x = x
        return segments
    
    def print(self):
        segments = self.__combine_dim(self.stride[0], self.mat)
        stride = self.stride
        for x in range(1, len(self.stride)):
            segments = self.__combine_dim(self.stride[len(self.stride) - x], segments)
            #stride.pop(len(self.stride) - x)
        segments = segments[0]
        for x in segments:
            print(x)

    def reshape(self, shape):
        pass

    def cat(self, mat):
        if type(mat) is not matrix:
            self.mat.append(mat)
        else:
            self.mat.append(mat.mat)

def matmul(matA, matB):
    pass
    

mat1 = matrix([3, 2, 3])
mat1.print()