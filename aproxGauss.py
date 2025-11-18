import math

a = int(input("Ingrese el valor de a: "))
deltaX = 20
deltaY = 4
nx = 2*a//deltaX
ny = 2**a//deltaY
aprox = 0
def f(x: int, y: int) -> float:
    return math.pow(math.e, -x**2-y**2)
for i in range(deltaY):
    for j in range(deltaX):
        aprox += f(-a + j*nx, -a + i*ny)
print(aprox)
