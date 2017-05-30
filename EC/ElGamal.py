from EC import *

class ElGamal(object):
    """ ElGamal encryption
    pub key encryption as repalcing 
    (mulmod,powmod) to (ec.add, ec.mul)
    - ec : ellitpic curve
    - g : (random) point on ec
    """
    
    def __init__(self):
        assert ec.is_valid(g)
        self.ec = ec
        self.g = g
        self.n = ec.order(g)
        pass

    def gen(self, priv):
        """generate a public key
        ret:pub key as point on ec
        """

        return self.ec.mul(g,priv)

    def enc(self,plain,pub,r):
        """encrypt
        plain : data as a point on ec
        pub: pub key as point on ec
        r: random int r<q
        ret (cipher1,cipher2)
        """

        assert self.ec.is_valid(plain)
        assert self.ec.is_valid(pub)
        return (self.ec.mul(g,r),self.ec.add(plain,self.ec.mul(pub,r)))

    def dec(self, cipher, priv):
        """decrypt
        cipher as points on ec
        priv: priv key as int < q
        ret plain as a point on ec
        """
        
        c1,c2 = cipher
        assert self.ec.is_valid(c1) and self.ec.is_valid(c2)
        return self.ec.add(c2, self.ec.neg(self.ec.mul(c1,priv)))

pass


