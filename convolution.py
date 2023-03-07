from numpy import array,linspace,zeros,roll,fliplr,append
from math import ceil
from sympy import symbols,sympify,lambdify
from matplotlib.pyplot import subplot,plot,title,show,stem
#Group2
class definer:
    '''This class defines the time axis and the bounds for the basic signals'''
    def __init__(self) -> None:
        self.x1=0#Lower limit of signal 1
        self.x2=20#Upper limit of signal 1
        self.h1=0#Lower limit of signal 2
        self.h2=20#Upper limit of signal 2
        self.t=array([])#Creating an empty array for time axis
        self.s=0#The size of time axis
        return
    def create_time_axis(self):
        '''This method returns a time axis'''
        self.xi1=self.x1+self.h1#Lower limit
        self.xi2=self.x2+self.h2#Upper limit
        #Creating the time axis
        if self.xi1>self.xi2:
            self.s=ceil(self.xi1)+ceil(self.xi1)+1
            self.t=linspace(-ceil(self.xi1),ceil(self.xi1),self.s)
        else:
            self.s=ceil(self.xi2)+ceil(self.xi2)+1
            self.t=linspace(-ceil(self.xi2),ceil(self.xi2),self.s)
        return self.t#Returning the time axis
class function_input:
    '''This class deals with the input of symbolic functions as numpy arrays'''
    def __init__(self) -> None:
        pass
    def __inp(self,string):
        '''This pvt method inputs the expression'''
        self.t = symbols('t')
        x =input(string)
        self.x=sympify(x)
    def make_array(self,time_axis,inp_prompt):
        '''This method returns an numpy array from the user input of a symbollic function'''
        self.__inp(inp_prompt)#inputing the function
        lam_x = lambdify(self.t, self.x, modules=['numpy'])
        self.y_vals = lam_x(time_axis)#putting the function value into a numpy array
        return self.y_vals
class sampler:
    '''This class samples a given signal'''
    def __init__(self) -> None:
        pass
    def sample(self,Signal,bounds,size):
        '''This method returns the sampled array'''
        Op_signal=zeros((1,size))
        for i in range(((size-1)//2)+bounds[0],((size-1)//2)+bounds[1]+1):
            Op_signal[0][i]=Signal[i]#for t∈(0,20) h(t)=t
        return Op_signal
class calculator:
    '''This class calculates the convolution of 2 signals'''
    def __init__(self,size) -> None:
        self.Y=zeros((1,size))  
        self.size=size
        pass
    def calculate(self,Signal1,Signal2,bounds):
        '''This method returns the convolution array of 2  arrays'''
        for i in range(bounds[0],bounds[1]+1):
            H1=fliplr(Signal2)  #flipping
            H1=roll(H1,i)  #shifting
            a=H1*Signal1  #scaling
            self.Y[0][((self.size-1)//2)+i]=sum(a[0]) 
        return self.Y
class Convolution:
    def __init__(self) -> None:
        pass
    def start(self):
        defin=definer()
        self.t=defin.create_time_axis()
        inputer=function_input()
        x=inputer.make_array(self.t,"Enter the first signal :")
        h=inputer.make_array(self.t,"Enter the second signal :")
        samp =sampler()
        self.x_samp=samp.sample(x,(defin.x1,defin.x2),defin.s)
        self.h_samp=samp.sample(h,(defin.h1,defin.h2),defin.s)
        calc=calculator(defin.s)
        self.conv_x_h=calc.calculate(self.x_samp,self.h_samp,(defin.xi1,defin.xi2))
            
    def graph(self):
        subplot(3,1,1)
        plot(self.t,self.x_samp[0])
        title("X(t)") 
        subplot(3,1,2)
        plot(self.t,self.h_samp[0])
        title("H(t)") 
        subplot(3,1,3)
        plot(self.t,self.conv_x_h[0])
        title("X(t)*H(t)") 
        show()
    
c=Convolution()
c.start()
c.graph()