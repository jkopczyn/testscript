#import necessary packages
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import norm

mu = 2*pow(10,5)
sig = 5*pow(10,4)
val = 3*mu

def create_buyer_likelihood(mean, stddev):
    def likelihood(x):
        return norm.sf(x, mean, stddev)
    return likelihood

buyer_likelihood = create_buyer_likelihood(mu, sig)

def insurer_risk(price, value):
    return buyer_likelihood(price)*value

def take_third(triple):
    return triple[2]

triples = ((price, buyer_likelihood(price), insurer_risk(price, val)) for price in xrange(0,10*mu, mu/10))



