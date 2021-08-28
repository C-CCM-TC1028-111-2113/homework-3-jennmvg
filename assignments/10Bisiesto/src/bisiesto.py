import math

anio= int(input("Ingrese un año:"))
def es_bisiesto ():
    if (anio%4 == 0) or (anio%400==0):
        print ("True")
    elif(anio%100==0) or (anio%4 !=0):
        print ("False")

def main():
  #escribe tu código abajo de esta línea
    es_bisiesto()
if __name__ == '__main__':
    main()
