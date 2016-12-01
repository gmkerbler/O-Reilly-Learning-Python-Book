#!/usr/bin/env python3

import math

def veccheck(x,y,z):
    """This function checks if diffusion vector scheme is appropriate"""

    x2, y2, z2 = (x**2), (y**2), (z**2)
    result = math.sqrt(x2+y2+z2)
    print ('VecCheck Result: ', result)

    if 0.98<result<1.01:
        print ('Vector is appropriate')
    else:
        print('Vector might be wrong..')

def vecconv(x,y,z,v):
    """This function converts the diffusion vector scheme by a scaling value"""

    xv, yv, zv = (x*v), (y*v), (z*v)
    xv2, yv2, zv2 = (xv**2), (yv**2), (zv**2)
    resultv = math.sqrt(xv2+yv2+zv2)
    print ('VecResult: ', resultv)

def veccalc(x,y,z,v):
    """This function checks a vector and scales a vector"""

    veccheckresult = veccheck(x,y,z)
    print('Vector check result: ', veccheckresult)

    vecscaleresult = vecconv(x,y,z,v)
    print('Vector scale result', vecscaleresult)
