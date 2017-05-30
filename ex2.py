from EC.EC import *

ec = EC(7,11,593899)

x = 12345
x *= 10 

messagelist = [i for i in xrange(x, x+10)]

for m in messagelist:
    
    p1,p2 = ec.at(m)
    
    if ec.is_valid(p1):
        print p1
    
    elif ec.is_valid(p2):
        print p2

pass

