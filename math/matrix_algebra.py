# Matrix Algebra
1.1:
import numpy as np
a = np.array([[1,2,3],[2,7,4]])
print a.ndim
=> 2
1.2:
import numpy as np
a = np.array([[1,-1],[0,1]])
print a.ndim
=> 2
1.3:
import numpy as np
a = np.array([[5,-1],[9,1],[6,0]])
print a.ndim
=> 2
1.4:
import numpy as np
a = np.array([[3,-2,-1],[1,2,3]])
print a.ndim
=>2
1.5:

import numpy as np
a = np.matrix([[1,2,3],[2,7,4]])
b = np.matrix([[1,-1],[0,1]])
c = np.matrix([[5,-1],[9,1],[6,0]])
d = np.matrix([[3,-2,-1],[1,2,3]])

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([1,8,0,5])

#Matrix Operations

try:
    aplusb = np.add(a,c)
    print "A + C = ",aplusb
except ValueError:
    print "A + C = Not Defined"


ct = np.transpose(c)
try:
    aminusct = np.subtract(a,ct)
    print "A - Ct = ", aminusct
except ValueError:
    print "A - Ct = Not Defined"

ddot = 3*d
try:
    cplusd = np.add(ct,ddot)
    print "Ct - 3d = ", cplusd
except ValueError:
    print "Ct + 3d = Not Defined"

print "BA = ", b.dot(a)

at = np.transpose(a)
try:
    bat = b.dot(at)
    print "BAt = ", bat
except ValueError:
    print "BA transpose = Not Defined"
"""Results:
A + C = Not Defined
A - Ct =  [[-4 -7 -3]
 [ 3  6  4]]
Ct - 3d =  [[14  3  3]
 [ 2  7  9]]
BA =  [[-1 -5 -1]
 [ 2  7  4]]
BA transpose = Not Defined
"""


#Vector Operations
uv = np.dot(u,v)
magu = np.linalg.norm(u)
print "u + v = ", u+v
print "u - v = ", u-v
print "au = ", 6 * u
print "uv = ", uv
print "Magnitude of u = ", magu
"""Results:
u + v =  [ 9  7 -4  9]
u - v =  [ 3 -3 -2  1]
au =  [ 36  12 -18  30]
uv =  51
Magnitude of u =  8.60232526704
"""
