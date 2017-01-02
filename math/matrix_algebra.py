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

Vector Operations:
import numpy as np
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([1,8,0,5])
uv = np.dot(u,v)
magu = np.linalg.norm(u)

print "u + v = ", u+v
print "u - v = ", u-v
print "au = ", 6 * u
print "uv = ", uv
print "Magnitude of u = ", magu


