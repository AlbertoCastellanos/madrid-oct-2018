import random
import numpy as np
def weird_mul(A, B):
    res=[[]]
    if all(i==0 for i in A.shape):
        return None
    elif all(i==0 for i in B.shape):
        return None
    elif len(A.shape) or len (B.Shape) != 2:
        return None
    else:
        res=np.multiply(A,B)
        return res

## I am not sure how to solve the problem I am receiving for some of the tests.
<<<<<<< HEAD
## "operands could not be broadcast together with shapes (2,2) (2,3)"
## Needed for loop to create weird multiplication
=======
## "operands could not be broadcast together with shapes (2,2) (2,3)"
>>>>>>> 01c97689353490e73a0e7b87f85a9cb04e57a999
