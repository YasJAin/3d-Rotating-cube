from math import *
import sys
import time
import os

A = B = C = 0

cubewidth = 10.0
width, height = 60, 44
distanceFromCam = 60
K1 = 40

incrementSpeed = 0.6

x = y = z = 0.0
ooz = 0.0
xp = yp = 0
idx = 0

def calculateX(i: int, j: int, k: int) -> float:
    return (j*sin(A)*sin(B)*cos(C) - k*cos(A)*sin(B)*cos(C) +
            j*cos(A)*sin(C) + k*sin(A)*sin(C) + i*cos(B)*cos(C))

def calculateY(i: int, j: int, k: int) -> float:
    return (j*cos(A)*cos(C) + k*sin(A)*cos(C) -
            j*sin(A)*sin(B)*sin(C) + k*cos(A)*sin(B)*sin(C) -
            i*cos(B)*sin(C))

def calculateZ(i: int, j: int, k: int) -> float:
    return (k*cos(A)*cos(B) - j*sin(A)*cos(B) + i*sin(B))

def calculateForSurface(cubeX: float, cubeY: float, cubeZ: float, ch: str):
    global x, y, z, ooz, xp, yp, K1, idx
    x = calculateX(cubeX, cubeY, cubeZ)
    y = calculateY(cubeX, cubeY, cubeZ)
    z = calculateZ(cubeX, cubeY, cubeZ) + distanceFromCam

    ooz = 1/z

    xp = int(width/2 + K1*ooz*x*2)
    yp = int(height/2 + K1*ooz*y)

    idx = xp + yp*width
    if idx >= 0 and idx < width*height:
        if ooz > zBuffer[idx//width][idx%width]:
            zBuffer[idx//width][idx%width] = ooz
            buffer[idx//width][idx%width] = ch


os.system("cls")
while True:
    zBuffer = [[0]*width for _ in range(height)]
    buffer = [[" "]*width for _ in range(height)]
    cubeX = -cubewidth
    while cubeX < cubewidth:
        cubeY = -cubewidth
        while cubeY < cubewidth:
            calculateForSurface(cubeX, cubeY, -cubewidth, ".")
            calculateForSurface(cubewidth, cubeY, cubeX, "$")
            calculateForSurface(-cubewidth, cubeY, -cubeX, "~")
            calculateForSurface(-cubeX, cubeY, cubewidth, "#")
            calculateForSurface(cubeX, -cubewidth, -cubeY, ";")
            calculateForSurface(cubeX, cubewidth, cubeY, "+")
            cubeY += incrementSpeed
        cubeX += incrementSpeed
    os.system("cls")
    for k in range(0, width*height, 1):
        sys.stdout.write(buffer[k//width][k%width] if k%width else chr(10))
    
    A += .005
    B += .005
    time.sleep(.001)
