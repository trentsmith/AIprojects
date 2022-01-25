import matplotlib.pyplot as plt
import math


# [equality for complex]
def ceq(a, b):
    return a.real == b.real and a.imag == b.imag

# [add, sub, mul for complex]
def cadd(a, b):
    a, b = complex(a), complex(b)
    return (a.real + b.real) + (a.imag + b.imag) * 1j

def csub(a, b):
    a, b = complex(a), complex(b)
    return (a.real - b.real) + (a.imag - b.imag) * 1j

def cmul(a, b):
    a, b = complex(a), complex(b)
    real = a.real * b.real - a.imag * b.imag
    imag = a.real * b.imag + a.imag * b.real
    return real + imag * 1j

print([cadd(1+1j, 2+2j), (1+1j) + (2+2j)])
print([cmul(1+1j, 2+2j), (1+1j) * (2+2j)])


# [div for complex]
def conj(c):
    c = complex(c)
    return c.real - c.imag * 1j
def norm(c):
    c = complex(c)
    return c.real * c.real + c.imag * c.imag
def cinv(c):
    c = complex(c)
    # 1/(a+i*b) = (a-i*b)/[(a+i*b)*(a-i*b)]
    #           = (a-i*b)/(a*a + b*b)
    base = norm(c)
    return (c.real / base) - (c.imag / base) * 1j

def cdiv(a, b):
    #return cmul(a, cinv(b))
    base = norm(b)
    c = cmul(a, conj(b))
    return (c.real / base) + (c.imag / base) * 1j

print([cdiv(1+2j, 2+1j), (1+2j) / (2+1j)])


# [pow for complex]
def c2p(c):
    c = complex(c)
    r = math.pow(norm(c), 0.5)
    theta = math.atan2(c.imag, c.real)
    return r, theta # "r" and "theta" also called as "abs" and "arg"
def p2c(r, theta):
    return r * math.cos(theta) + r * math.sin(theta) * 1j

def cpow(a, b):
    r, t = c2p(a)
    b = complex(b)
    c, d = b.real, b.imag
    # a^b = (r*exp(i*t))^(c+i*d)
    #     = r^(c+i*d) * (exp(i*t))^(c+i*d)
    #     = r^c * r^(i*d) * exp(-d*t + i*c*t)
    #     = r^c * exp(log(r) * i*d) * exp(-d*t + i*c*t)
    #     = r^c * exp(log(r) * i*d -d*t + i*c*t)
    #     = r^c * exp(-d*t) * exp(i*(d*log(r) + c*t))
    #     = r^c * exp(-d*t) * [cos(d*log(r) + c*t) + i*sin(d*log(r) + c*t)]
    R = math.pow(r, c) * math.exp(-d * t)
    T = d * math.log(r) + c * t
    return p2c(R, T)

print([cpow(1+2j, 2+1j), (1+2j) ** (2+1j)])
print([cpow(2, 3), (2+0j) ** (3+0j)])


# [exp, log for complex]
def cexp(c):
    #return cpow(math.e, c)
    # exp(a+i*b) = exp(a) * exp(i*b)
    #            = exp(a) * [cos(b) + i*sin(b)]
    c = complex(c)
    return p2c(math.exp(c.real), c.imag)
    
def clog(c, n=0):
    r, t = c2p(c)
    # log(r*exp(i*t)) = log(r) + log(exp(i*t))
    #                 = log(r) + i*(t + 2*PI*n)
    # (n = ..., -2, -1, 0, +1, +2, ...)
    return math.log(r) + (t + 2 * n * math.pi) * 1j
 
print(cexp(clog(1+1j)))
print(clog(cexp(1+1j)))

# [Riemann sphere projection (single infinity)]
def cproj(c):
    inf = float("inf")
    if c.real == inf or c.real == -inf or c.imag == inf or c.imag == -inf:
        return complex("inf")
    return c
# x axis values
from itertools import count, islice

def binom(n, k):
    v = 1
    for i in range(k):
        v *= (n - i) / (i + 1)
    return v


def zeta(s, t=100):
    if s == 1: return complex("inf")
    term = (1 / 2 ** (n + 1) * sum((-1) ** k * binom(n, k) * (k + 1) ** -s 
                                   for k in range(n + 1)) for n in count(0))
    return sum(islice(term, t)) / (1 - 2 ** (1 - s))


# [correct data with numpy]
import numpy

x = numpy.arange(-3, 3, 0.1)
y = numpy.arange(-30, 30, 1)
X, Y = numpy.meshgrid(x, y)

@numpy.vectorize
def z(real, imag):
    r = zeta(real + imag * 1j).real
    return min(max(-10, r), 10)

Z = z(X, Y)
#print(Z)


# [plot with matplotlib]
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot, cm

fig = pyplot.figure()
ax = fig.gca(projection="3d")
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, 
                       linewidth=0, antialiased=False)
ax.set_zlim(-10, 10)


from itertools import count, islice


# Basic definition of zeta func
# zeta(s) = sum(1/n^s)
# (Re(s) > 1)
def zeta1(s, t=10000):
    term = (1 / (n ** s) for n in count(1))
    return sum(islice(term, t))


print(zeta1(2)) # => 1.6449...
print((zeta1(2) * 6) ** 0.5) # => PI = 3.1415...
#print(zeta1(0.5+14.134725142j)) # invalid


# formula (20) in http://mathworld.wolfram.com/RiemannZetaFunction.html
#
#   sum((-1)^n/n^s) + sum(1/n^2) = 2 * sum(1/n^s, n=2,4,6,...)
#                                = 2 * sum(1/(2*n)^s)
#                                = 2 * 2^-s * sum(1/n^s)
#
#   sum((-1)^n/n^s) + zeta(s) = 2^(1-s) * zeta(s)
#
#   zeta(s) = 1/(1 - 2^(1-s)) * sum((-1^(n-1)) / n^s)
#   (Re(s) > 0 and s != 1)
def zeta2(s, t=10000):
    if s == 1: return float("inf")
    #term = ((-1)**(n - 1) / (n ** s) for n in count(1))
    #return sum(islice(term, t)) / (1 - 2**(1 - s))
    term = ((-1) ** n * n ** -s for n in count(1))
    return sum(islice(term, t)) / (2 ** (1 - s) -  1)


print(zeta2(2))
print((zeta2(2) * 6) ** 0.5)
print(abs(zeta2(0.5+14.134725142j))) # => 0
print(abs(zeta2(0.5-14.134725142j))) # => 0
#print(zeta2(0)) # invalid

# (utility) binomial coefficient
def binom(n, k):
    v = 1
    for i in range(k):
        v *= (n - i) / (i + 1)
    return v

# formula (21) in http://mathworld.wolfram.com/RiemannZetaFunction.html
# Global zeta function by Knopp and Hasse (s != 1)
def zeta3(s, t=100):
    if s == 1: return float("inf")
    term = (1 / 2 ** (n + 1) * sum((-1) ** k * binom(n, k) * (k + 1) ** -s 
                                   for k in range(n + 1)) for n in count(0))
    return sum(islice(term, t)) / (1 - 2 ** (1 - s))

print(zeta3(2))
print((zeta3(2) * 6) ** 0.5)
print(abs(zeta3(0.5+14.134725142j))) # => 0
print(abs(zeta3(0.5-14.134725142j))) # => 0
print(zeta3(1)) # => inf
print(zeta3(0)) # => -1/2
print(zeta3(-1)) # => -1/12 = 0.08333...
print(zeta3(-2)) # => 0
pyplot.show()