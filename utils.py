import random

def inv(n,q):
    """ from Euler Totient Function an inverse modulo function
        - n * (q-1) % q = 1 => n ** (q-2) % n = n ** -1 % q
    """

    assert q > 2
    s,p2, p = 1,n, q-2
    while p > 0:
        if p & 1 == 1 :
            s = s * p2 % q
        #when pow has three args it rets (p2^2) mod q
        p, p2 = p >> 1, pow(p2,2,q)
        pass
    return s

def sqrt(n,q):
    """Sqrt mod for big ints
       -Algorithm 3.34 of [2], Chapter 3
       Jacoby symbol is def below
    """
    b = 0
    while b == 0 or jacobi(b,q) == -1:
        b = random.randint(1,q-1)
        pass
    t,s = q-1,0
    while t & 1 == 0:
        t,s = t >> 1, s + 1
        pass
    assert q == t * pow(2,s) + 1 and t % 2 == 1
    ni = inv(n,q)
    c = pow(b,t,q)
    r = pow(n, (t+1) // 2, q)
    for i in xrange(1,s):
        d = pow(pow(r,2,q) * ni % q,pow(2, s- i -1 , q),q)
        if d == q - 1 : r = r*c % q
        c = pow(c,2,q)
        pass
    return (r, q-r)

def jacobi(b,q):
    """A quick implementation of the Jacobi symbol
    please refer to algorithm 2.149 of [2] chap2.pdf
    """
    if a == 0 : return 0
    if a == 1 : return 1
    a1,e = a,0
    while a1 & 1 == 0:
        a1,e = a1 >> 1 , e + 1
        pass
    m8 = q % 8
    s = -1 if m8 == 3 or m8 == 5 else 1
    #m8 is 0,2,4,6 or 1,7
    if q % 4 == 3 and a1 % 4 == 3: s = -s
    return s if a1 == 1 else s * jacobi(q % a1, a1)


