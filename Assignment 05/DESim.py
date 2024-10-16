import math

a = 7**5
g = 2**31-1
A = 933588178
S = 209208115
Ta = 200
Ts = 100

# Random Number Generator
def ranfA():
    global A 
    A = a * A % g
    return A/g

def ranfS():
    global S
    S = a * S % g
    return S/g

# Exponential Routine
def expntl(t):
    if t == Ts:
        return -t * math.log(ranfS())
    if t == Ta:
        return -t * math.log(ranfA())

# Sim Code
te = t2 = 10000000
n = t1 = tn = tb = time = 0
B = C = s = 0

while (time < te):
    if (t1 < t2):
        # event 1: arrival
        time = t1
        s += n * (time - tn)
        n+=1
        tn = time
        t1 = time + expntl(Ta)
        if (n == 1):
            tb = time 
            t2 = time + expntl(Ts)
        # print(f'Ts: {t1}, {t2}')
        # print(f'Time: {time}, {tb}')
    else:
        # event 2: completion
        time = t2
        s += n * (time - tn)
        n-=1
        tn = time
        C+=1
        if (n > 0): 
            t2 = time + expntl(Ts)
        else: 
            t2 = te
            B += time - tb
        # print(f'Ts: {t1}, {t2}')
        # print(f'Time: {time}, {tb}')

# Results
X = C / time
print(f'throughput = {X}')
U = B / time
print(f'utilization = {U}')
L = s / time
print(f'mean no. in system = {L}')
W = L / X
print(f'mean residence time = {W}')