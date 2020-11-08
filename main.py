#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

PI = "3.14159265358979323846"  # hardcoded value of pi

# computation constants
DIGITS = 8  # digits of π to compute
MA = 100 ** (DIGITS - 1)  # mass block A
MB = 1  # mass block B

# computation variables
vb_c = 0  # Velocity block B current phase
va_c = -1  # Velocity block A current phase
vb_p = 0  # Velocity block B previous phase phase
va_p = -1  # Velocity block A previous phase
phase = 1  # phase

start_time = time.time()

while True:
    if vb_c < 0:
        vb_c = vb_c * -1

    else:
        vb_c = (2 * va_p * MA / MB + (1 - MA / MB) * vb_p) / (1 + MA / MB)
        va_c = (2 * vb_p * MB / MA + (1 - MB / MA) * va_p) / (1 + MB / MA)

    if (vb_c >= 0) and (va_c > 0) and (vb_c < va_c):
        break

    # Moving current velocities into previous velocity for next phase
    vb_p = vb_c
    va_p = va_c

    # Next phase
    phase += 1

print("Done after " + str(phase) + " phases")

π = str(phase * 0.1 ** (DIGITS - 1))[: DIGITS + 1]  # calculated value of pi
print("π ≈ {0}".format(π))
PI_TRIMMED = PI[: DIGITS + 1]  # let PI be the same length as π

if π != PI_TRIMMED:
    print("Error, value does not match")
    print("{0} ≠ {1}".format(π, PI_TRIMMED))

print("Done in {0:.3} seconds".format(time.time() - start_time))
