
def calculate_series(length, better_probability=0.5):
    previous = [0,0]
    print "\t".join(map(str,previous))
    for i in range(length):
        previous = [0] + [1+previous[j]*better_probability+previous[j+1]*(1-better_probability) for
                j in range(len(previous)-1)] + [0]
        print "\t".join(map(str,previous))
    return previous[(length+1)/2]

print calculate_series(7)

##sanity check that the results make sense in an edge case
#print calculate_series(7, 0.999999)

print calculate_series(7, 0.6)
print calculate_series(7, 0.7)
