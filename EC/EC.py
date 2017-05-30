import collections

Coord = collections.namedtuple("Coord", ["x","y"])

from utils import *

class EC(object):
    """Elliptic Curve"""
    def __init__(self,a,b,q):
        """elliptic curves as (y^2 = x^3 + a*x + b) mod q
        a,b params of curve
        q prime int
        """
        assert a > 0 and a < q and b > 0 and b < q and q > 2
        assert (4*(a**3) * 27*(b**2)) % q != 0

        self.a = a
        self.b = b
        self.q = q

        self.zero = Coord(0,0)

        pass

    def is_valid(self,p):
        """checks if p belongs to ec"""
        if p == self.zero : return True
        l = (p[1]**2) % self.q
        r = ((p[0]**3) + (self.a * p[0]) + self.b) % self.q
        return l == r

    def at(self,x):
        """finds point on ec at x"""
        assert x < self.q
        ysq = (x**3 + self.a * x + self.b) %  self.q
        y,my = sqrt(ysq, self.q)
        return Coord(x,y) , Coord(x,my)

    def neg(self,p):
        return Coord(p[0], -p[1] % self.q)

    def add(self,p1,p2):
        
        if p1 == self.zero :  return p2
        if p2 == self.zero :  return p1

        if p1[0] == p2[0] and (p1[1] != p2[1] or p1[1] == 0):
            return self.zero

        if p1[0] == p2[0]:
            l = (3 * p1[0] ** 2 +self.a) * inv(2*p1[1], self.q) % self.q
            pass
        else:
            l = (p2[1]-p1[1]) * inv (p2[0] -p1[0], self.q) % self.q
            pass

        x = (l*l -p1[0] - p2[0]) % self.q
        y = (l*(p1[0] -x)-p1[1]) % self.q

        return Coord(x,y)

    def mul(self,p,n):
        r = self.zero
        m2 = p
        #O(log2(n)) addition
        while 0 < n:
            if n & 1 == 1:
                r = self.add(r,m2)
                pass
            n,m2 = n>>1, self.add(m2,m2)
            pass
        return r

    def order(self,p):
        assert self.is_valid(p) and  p != self.zero
        hasse = self.q
        for i in xrange(1, hasse +1):
            if self.mul(p,i) == self.zero:
                return i
            pass
        pass
        
        raise Exception("Invalid order")
        pass

