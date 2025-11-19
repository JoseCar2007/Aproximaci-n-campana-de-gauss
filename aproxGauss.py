import math

a = int(input("Ingrese el valor de a: "))
nx = 20
ny = 4
deltaX = 2*a//nx
deltaY = 2**a//ny
aprox = 0
def f(x: int, y: int) -> float:
    return math.pow(math.e, -x**2-y**2)
for i in range(ny):
    for j in range(nx):
        aprox += f(-a + j*deltaX, -a + i*deltaY)*nx*ny
print(aprox)
