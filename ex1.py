from EC import *

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

#result5 = ec.order(p1)
#print result5

test = ec.mul(p1,20)
print (test == ec.zero)
