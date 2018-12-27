#import necessary packages
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import norm
from itertools import imap

def quantify(iterable, predicate=bool):
    return sum(imap(predicate, iterable))


p5thresh = norm.interval(0.9)[0]
p01thresh = norm.interval(0.998)[0]
isp01 = lambda x: x <= p01thresh

runs = 1
samples = 10000
for i in xrange(runs):
    xs = []
    while len(xs) < samples:
        cand = norm.rvs()
        if cand <= p5thresh:
            xs.append(cand)
    
    count = quantify(xs, isp01)
    print count*(100.0/samples)
    
