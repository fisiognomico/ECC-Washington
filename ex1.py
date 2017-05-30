from EC.EC import *

ec = EC(2,3,19)

p1 = (1,5)

p2 = (9,3)

result1 = ec.add(p1,p2)

print result1

negp2 = ec.neg(p2)

result2 = ec.add(p2,negp2)

print result2

result3 = ec.add(p1,negp2)

print result3

k = 1

while(True):
    k += 1
    result4 = ec.mul(p1,k)
    if (result4 == p2):
        print k
        break

result5 = ec.order(p1)
print result5

##For part 6 we can reason in this way
##Using Lagrange Thm (Group Theory) we
##can prove that the number of points 
## on EC is a multiple of the order of P
##Using g for order of P
## N = k * g for some k
##Using Hasse Thm we know that
##abs(N - q -1) < 2*sqrt(q)
##So knowing that N must be less than ~28
##the factor k must be 1
## So the  number of points on EC is 20
