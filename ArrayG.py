# This is a Python library that aims to provide basic assistance 
# in working with arrays using numpy.
# ------
# Created by Gael Etchebest (finoliso on GitHub).

import numpy as np

class Arr:
    def __init__(self, size, type):
        self.size = size
        self.type = type
        self.__array = np.zeros(size, type)
    
    def __str__(self):
        return f"{self.__array}"

    def getValue(self, place):
        if not isinstance(place, int):
            raise Exception("Arr: Place must be of type int.")
        if place < self.size and place >= self.size * -1:
            return self.__array[place]
        raise Exception("Arr: Place has exceeded the range.")

    def __verifyValue(self, value):
        if isinstance(value, self.type):
            return value
        else:
            raise Exception(f"Arr: The input variable is not of the corresponding type.")

    def set_place(self, place, value):
        self.__array[place] = self.__verifyValue(value)
    
    def set(self, value):
        if not isinstance(value, np.ndarray):
            raise Exception("Arr: Value must be of type numpy array.")
        valueType = float
        if len(value) > 0:
            valueType = Arr.__getTypeValue(value[0])
            
        if not valueType == self.type:
            raise Exception(f"Arr:The array type is not an {self.type} type.")
            
        self.__array = value
        self.size = len(self.__array)

    def __getTypeValue(value):
        try:
            valueType = type(value.tolist())
        except:
            valueType = type(value)
        return valueType

    def add(self, value):
        value = self.__verifyValue(value)
        array1 = np.zeros(self.size + 1, self.type)
        for i in range(self.size): 
            array1[i] = self.__array[i]
        array1[-1] = value
        self.__array = array1
        self.size += 1
    
    def remove(self, place):
        if not isinstance(place, int):
            raise Exception(f"Arr: Remove only accepts int type.")
        array1 = np.zeros(self.size - 1, self.type)
        n1 = 0
        for i in range(self.size - 1):
            if i == place:
                n1 = 1
            array1[i] = self.__array[i+n1]
        self.__array = array1
        self.size -= 1
