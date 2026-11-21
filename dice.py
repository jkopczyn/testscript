import random

def roll(die=20, num=1):
    print [random.randint(1, die) for idx in xrange(num)]
        
