import math

def rectangulo ():
    base= float(input("Dame la base:"))
    altura= float (input("Dame la altura:"))
    area= float(base*altura)
    return area 



areaBase= float(rectangulo())
profundidad= float (input("Dame la profudidad:"))
volumen= areaBase*profundidad
print ("El volumen del prisma es:", volumen)
