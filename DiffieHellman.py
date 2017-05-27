from EC import *

class DiffieHellman(object):
    """EC DiffieHellman (key agreement)
    ec: elliptic curve
    g : a point on ec
    """

    def __init__(self):
        self.ec = ec
        self.g = g
        self.n = ec.order(g)
        pass

    def gen(self,priv):
        """Generates a public key
        out of a priv one
        priv: a point on ec
        """

        assert priv > 0 and priv < self.n
        return (self.ec.mul(self.g,priv))

    def secret(self,priv,pub):
        """calc screte shared key for the pair
        priv : my private key on ec
        pub : partner's secret key on ec
        ret : shared secret key on ec
        """
        assert self.ec.is_valid(pub)
        assert self.ec.mul(pub, self.n) == self.ec.zero
        return self.ec.mul(pub,priv)

    pass

