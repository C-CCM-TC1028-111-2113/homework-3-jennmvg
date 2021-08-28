import math

def max():
    papel= int(input("Dame la cantidad de pliegos de papel albanene:"))
    plumones= int(input("Dame la cantidad de plumones:"))
    if (papel>=plumones) or (papel*12<=35):
        tarjetas= plumones*35
        print("El número máximo de tarjetas que se pueden hacer es:", tarjetas)
    elif (papel<plumones):
        tarjetas= papel*12
        print("El número máximo de tarjetas que se pueden hacer es:", tarjetas)
    else:
        print ("invalid")

def main():
  #escribe tu código abajo de esta línea
    max()
if __name__ == '__main__':
    main()
