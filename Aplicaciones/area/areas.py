import math



def area_cuadrado(L):
    
    area=L**2
    return  print('el area del cuadrado es: ', area)


def area_circulo(R):
    
    area=math.pi*R**2
    return print('el area del circulo es %.3f ' % area)

def area_triangulo(b,h):

    area=b*h/2
    return print('El area del triángulo es: ', area)

def area_trapecio(B,b,h):

    area=(B+b)*h/2
    return print('El area del Trapecio es: ', area)

def area_rectangulo(b,h):

    area=b*h
    return print('El area del Rectángulo es: ', area)

def area_elipse(a,b):

    area=a*b*math.pi
    return print('El area de la elipse es %.3f ' % area)

import areas

print("Calcular Áreas de figuras Geométricas.\n")
print("1.Cuadrado.\n2.Circulo.\n3.Triángulo.\n4.Trapecio.\n5.Rectángulo.\n6.Elipse.\n")

x=int(input("Escoja la figura: "))

if x==1:
    L=int(input('Ingrese el lado: '))
    areas.area_cuadrado(L)
    
if x==2:

    R=int(input('Ingrese el radio del circulo: '))
    areas.area_circulo(R)
    
if x==3:
    
    b=int(input('Ingrese la base: '))
    h=int(input('Ingrese la altura: '))
    areas.area_triangulo(b,h)
   
if x==4:
    
    B=int(input('Ingrese la base 1:'))
    b=int(input('Ingrese la base 2: '))
    h=int(input('Ingrese la altura: '))
    areas.area_trapecio(B,b,h)
    
if x==5:
    
    b=int(input('Ingrese la base: '))
    h=int(input('Ingrese la altura: '))
    areas.area_rectangulo(b,h)
    
if x==6:
    
    a=int(input('Ingrese el eje menor: '))
    b=int(input('Ingrese el eje mayor: '))
    areas.area_elipse(a,b)
