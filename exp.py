import numpy as np 
from scipy.integrate import quad

mean= int(input("Enter the mean:"))

def f(x,mean):
    return (1/mean)* np.exp(-(1/mean)*x)
    
lower_lim=int(input("Enter the lower limit (Enter 0 if -infinity):"))
upper_lim=int(input("Enter the upper limit (Enter 0 if infinity):"))

if lower_lim==0: # lower limit -infinity
    expo_pdf=quad(f,0,upper_lim, args=(mean))  # -infinity to y is same as 0 to y
    print("The exponential probability value is:", expo_pdf)

elif upper_lim==0: #upper limit is infinity
    pos_inf=float('inf')
    expo_pdf=quad(f,lower_lim,pos_inf, args=(mean))  # x to +infinity
    print("The exponential pdf is:", expo_pdf)

else:
    expo_pdf=quad(f,lower_lim, upper_lim, args=(mean)) # from lower to upper limit
    print("The exponential pdf is:", expo_pdf)
