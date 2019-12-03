#!/usr/bin/env python

import time
import math
import numpy
import darts
#import cpdarts

def main ():
    """Time result of Monte--Carlo calculations for a number of sample sizes (log spacing)"""

    # generate values for number of tries

    NVals = numpy.logspace (1, 8, base=10.0, num=6, dtype=numpy.int)

    # List of implementations
    intFuncList = [ 
                 (darts.numQuadrantHitsPython, "darts_python.txt"),
		 (darts.numQuadrantHitsNumPy,  "darts_numpy.txt"),
		 (darts.numQuadrantHitsNumba,  "darts_numba.txt"),
#		 (cpdarts.numQuadrantHits,     "darts_cython.txt")
               ]

    for intFunc, file in intFuncList:

	# Open results file...

	fh =  open( file, "w" ) 

    	# compute Pi 
	for numPoints in NVals:
        	t1 = time.time ()
    	     	n1 = intFunc (numPoints)
	     	e1 = math.fabs (4.0 * float (n1) / float (numPoints) - math.pi)
    	     	t1 = time.time () - t1
	     	fh.write("{:d} {:6.4g}\n".format(numPoints, t1))
	fh.close()


if __name__ == "__main__":
    main ()
