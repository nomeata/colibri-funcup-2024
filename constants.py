import math

schaui = (47.90982,7.88921)
landepunkt = (47.9328569,7.864453)

# flugendesinken in m/s
flightstop = 0.5

# segment definition
rings = 15
r0 = 0.5
dr0 = 0.5
drf = 2**(1/4)

radius = [r0 + dr0 * (drf**i - 1)/(drf-1) for i in range(rings) ]
segments = [ 2**(round(math.log(2*math.pi*(radius[i]+radius[i+1])/2 / (radius[i+1]-radius[i]), 2))) for i in range(rings-1) ]
offset = [0 for i in range(rings-1)]
for i in range(1,rings-1):
    offset[i] = offset[i-1] + 0.5 * 260/segments[i]
