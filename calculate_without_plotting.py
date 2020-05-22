#!/usr/bin/env python
# -*- coding: utf-8 -*-

TIME_IT = True
if TIME_IT:
    import time

    START_TIME = time.time()

# computation constants
DIGITS = 6  # digits of π to compute
MA = 100 ** (DIGITS - 1)  # mass block A
MB = 1  # mass block B
PI = "3.14159265358979323846"  # hardcoded value of pi

# computation variables
vb_c = 0  # Velocity block B current phase
va_c = -1  # Velocity block A current phase
vb_p = 0  # Velocity block B previous phase phase
va_p = -1  # Velocity block A previous phase
n = 1  # phase
stop = False  # stop condition

while not stop:
    if vb_c < 0:
        vb_c = vb_c * -1

    else:
        vb_c = (2 * va_p * MA / MB + (1 - MA / MB) * vb_p) / (1 + MA / MB)
        va_c = (2 * vb_p * MB / MA + (1 - MB / MA) * va_p) / (1 + MB / MA)

    if (vb_c >= 0) and (va_c > 0) and (vb_c < va_c):
        stop = True
        break

    # Moving current velocities into previous velocity for next phase
    vb_p = vb_c
    va_p = va_c

    # Next phase
    n += 1

print("done after " + str(n) + " phases")

π = str(n * 0.1 ** (DIGITS - 1))[: DIGITS + 1]  # calculated value of pi
print("π ≈ {0}".format(π))
PI_REDUCE = PI[: DIGITS + 1]  # let PI be the same length as π

if π == PI_REDUCE:
    print("excelent")
else:
    print("Error value does not match")
    print("{0} ≠ {1}".format(π, PI_REDUCE))

if TIME_IT:
    print("done in {0:.3} seconds".format(time.time() - START_TIME))
