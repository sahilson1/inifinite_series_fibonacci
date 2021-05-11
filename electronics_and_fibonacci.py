import math

#infinite resestive n/w
"""
It's a resistor ladder network which goes till infinity (THIS IS THE MOST IMPORTANT PART) and its equation is given by:
"""
x=1 # assuming the resistance of each resistor to be 1 ohm
y=(x*x) -x -1
#solution of the n/w
"""
The solution of the above equation is given by the quadratic formula: (-b +- sqrt(b*b - 4*a*c)) / (2*a)
where, a=1,b=-1 and c=-1
"""
a,b,c=1,-1,-1

y = (-b + (math.sqrt(b*b - 4*a*c)))/ (2*a)
print(y)
y = (-b - (math.sqrt(b*b - 4*a*c)))/ (2*a)
print(y)

#linking with fibonacci

"""
The first solution of this equation gives us the EXACT value of the golden ratio phi(ɸ).This is astounding finding the patterns 
everywhere 
"""

