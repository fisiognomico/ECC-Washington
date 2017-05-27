from EC import *

class DSA(object):
    """ECDSA
    ec: elliptic curve
    g : random point
    """
    def __init__(self,ec,g):
        self.ec = ec
        self.g = g
        self.n = ec.order(g)
        pass

    def gen(self,priv):
        """generate pub key)
        """
        assert priv > 0 and priv < self.n
        return self.ec.mul(self.g,priv)

    def sign(self,hashval,priv,r):
        """generate signature
        hashval : value of file to be sign
        priv : priv key on ec
        r : random int
        ret signature as (int,int)
        """
        assert r > 0 and r < self.n
        m = self.ec.mul(self.g,r)
        return (m.x, inv(r,self.n) * (hashval + m.x * priv ) % self.n)

    def validate(self, hashval, sig,pub):
        """ valudate signature
        -hashval message as int
        - sig signature as (int,int)
        - pub key as point on ec
        """

        assert self.ec.is_valid(pub)
        assert self.ec.mul(self.n,pub) == self.ec.zero
        
        w = inv(sig[1],self.n)
        u1, u2 = hashval * w % self.n , sig[0] * w % self.n
        p = self.ec.add(self.ec.mul(self.g,u1, self.ec.mul(pub,u2)))
        return p.x % self.n == sig[0]
    pass

