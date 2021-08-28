import math
def area():
    base= float (input("Dame la base:"))
    altura= float (input("Dame la altura:"))
    area= float(base*altura)
    return area

def main():
  #escribe tu código abajo de esta línea
    print ("El área del rectángulo es:", area())
    pass
if __name__ == '__main__':
    main()
