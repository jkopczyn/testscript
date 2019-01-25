import random

def fdf():
    df = [-1,0,1]
    s = 0
    for i in xrange(4):
        s += random.choice(df)
    return s

techs = {-4: "Stone Age", -3: "Metallurgy", -2: "Industrialization",
        -1: "Atomic power", 0: "Exploring the system",
        1: "Exploiting the system", 2: "Slipstream use", 3: "Slipstream mastery"
        , 4: "On the verge of collapse"}

envs = {4: "Many garden worlds", 3: "Some garden worlds", 
        2: "One garden and several survivable worlds", 
        1: "One garden and several hostile environments",
        0: "One garden world (perhaps additional barren worlds)",
        -1: "Survivable world",
        -2: "Hostile environment (gravity but dangerous athmosphere)",
        -3: "Barren world (gravity, no athmosphere)",
        -4: "No habitable gravity or athmosphere"}

resos = {4: "All you could want", 3: "Multiple exports",
        2: "One significant export", 1: "Rich", 0: "Sustainable",
        -1: "Almost viable", -2: "Needs imports", -3: "Multiple dependencies",
        -4: "No resources"}

def sysgen(num=1):
    systems = []
    for i in xrange(num):
        tech, env, res = fdf(), fdf(), fdf()
        systems.append(translate(tech, env, res))
    return systems

def translate(t,e,r):
    return ((t,e,r),(techs[t], envs[e], resos[r]))

def clustergen(num=6):
    sys = sysgen(num)
    conns = []
    incoming = {}
    for i in xrange(1,num+1):
        incoming[i] = 0
    for i in xrange(1,num):
        conn = fdf()
        incoming[i+1] += 1
        conns.append((i,i+1))
        if conn > 0 and next_isolate(incoming, i):
            j = next_isolate(incoming, i)
            conns.append((i,j))
            incoming[j] += 1
        if conn >= 0 and next_isolate(incoming, i):
            j = next_isolate(incoming, i)
            conns.append((i,j))
            incoming[j] += 1
    return (sys, conns)


def next_isolate(incoming, n):
    m = max(incoming.keys())
    for i in xrange(n+1,m+1):
        if incoming[i] == 0:
            return i
    return None


print clustergen(9+fdf())
