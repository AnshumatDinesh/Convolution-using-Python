import numpy
import math
import matplotlib.pyplot
import sympy
class function_maker:
    def __init__(self) -> None:
        self.t=sympy.symbols('t')
        
        pass
    def read(self):
        exp=input("Enter a function in terms of t: ")
        self.exp=sympy.sympify(exp)
        self.n=int(input("Enter the maximum limit of k: "))
        self.w=int(input("Enter the angular frequency: "))
        self.T=(2*numpy.pi)/self.w
    def calculate(self):
        s=sympy.fourier_series(self.exp,(self.t,0,self.T))
        self.series=s 
    def output(self):
        np_x=numpy.linspace(0,self.T)
        m=int(input("Enter the number of terms to be calculated: "))
        s1=self.series.truncate(n=m) 
        p=sympy.plot(self.exp,s1,show=True)
        