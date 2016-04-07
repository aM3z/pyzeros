class bisectionMethod():
    '''This is an implementation of the bisection method for locating zeros of
    functions.
    
    The bisection method exploits the Intermediate-Value Theorem, which states
    that if the function f is continuous on the closed intercal [a,b], and if
    f(a)<=y<=f(b) or f(b)<=y<=f(a), then there exists a point c such that 
    a<=c<=b and f(c)=y.
    
    At each step of this algorithm, there is an interval [a,b] and the values 
    u=f(a) and v=f(b) such that the product u*v is less than 0. Next, the 
    midpoint of the interval, c=(a + b)/2, is computed and w=f(c). This results 
    in one of three cases:
    
    Case 1. It can happen that f(c)=0.
    
    Case 2. If w*u < 0, one can be sure that a root of f exists in the interval
    [a,c].  So, the value of c is stored b and w in v. 
    
    Case 3. If w*u > 0 and w*v < 0, f must have a root in the interval [c,b]. 
    So, the value of c is stored a and w in u.
    
    If case 1, the algorithm stops. If case 2 or 3, the algorithm repeats until
    the interval is satisfactorily small. At the end, the best estimate of the 
    root would be (a + b)/2, where [a,b] is the last interval in the procedure.
    
    Args:
        f (function):
        a (real):
        b (real):
        nmax (int):
        error (real):
    
    Returns:
        bestEstimate (real):
    
    Raises:
    
    '''
    
    def __init__(self):
    # use fa, fb, fc as mnemonics for u, v, w, respectively
    # fa <- f(a)
    # fb <- f(b)
    # if sign(fa)=sign(fb) then
        # output a, b, fa, fb
        # output "function has same signs at a and b"
        # return
    # end if
    # error <- b - a
    # for n=0 to nmax
        # error <- error/2
        # c <- a + error
        # fc <- f(c)
        # output n, c, fc, error
        #if |error| < epsilon then
            # output "convergence"
            # return
        # end if
        # if sign(fa) != sign(fb) then
            # b <- c
            # fa <- fc
        #end if
    # end for
    
class newtonsMethod():
    
    def __init__(self):

class secantMethod():
    
    def __init__(self):
        
# see https://docs.python.org/2/tutorial/modules.html#executing-modules-as-scripts
if __name__ == "__main__":
    import sys
    # bisectionMethod(sys.argv[])
    # newtonsMethod(sys.argv[])
    # secantMethod(sys.argv[])