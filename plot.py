import numpy as np
import matplotlib.pyplot as plt

#defining x and y
x= np.linspace(-10, 10, 100)
y= x*x -x -1

#assigning the plotsize
fig = plt.figure(figsize = (10, 5))

#plot parameters
plt.plot(x,x*0,linestyle ='-')
plt.plot(x,y)
plt.annotate('ɸ',(1,1.6180355))
plt.grid(alpha = .4,linestyle ='--')
plt.xlabel('--------x-------->')
plt.ylabel('--------x*x -x -1-------->')
plt.title('FINDING ɸ IN RESISTOR INFINITE SERIES')
plt.show()
