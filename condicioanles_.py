# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:04:20 2021

@author: riber
"""
#ej1
total = int(input("¿Cuantas camisas usted va a llevar?: "))
if (total <= 0):
    print("Digite una cantidad valida!")
elif (total <= 2):
    print("Usted tendra un descuento del 10% amigo!")
else:
    print("Usted tendra un descuento del 30% en el total de su compra")
    
#ej2
numP = int(input("Digite un numero al alzar para obtener su promoción!: "))
if (numP <= 0):
    print("Un numero!")
elif (numP <= 73):
    print("Usted tendra un descuento del 15%!")
else:
    print("Usted tendra un descuento del 20%!")
    
#ej3
montoF = int(input("Digite el monto para la fianza: "))
if (montoF <= 0):
    print("No se puede determinar la cuota que debe pagar!")
elif (montoF <= 49999):
    print("El cliente debera pagar la cuota por un valor de: ",(montoF * 0.03))
else:
    print("El cliente debera pagar la cuota por un valor de: ",(montoF * 0.02))
    
#ej4
puntosF = int(input("Digite cuantos puntos cree que tiene su fabrica: "))
if (puntosF <= 0):
    print("Digite un valor valida!")
elif (puntosF <= 169):
    print("Su fabrica no tendra sancion ni multa.")
else:
    print("Usted sera sancionado con parar su produccion por una semana y una multa del 50% cuando no se detiene la produccion")

#ej5
precio = int(input("Digite el valor del carro que desea comprar: "))
incTerreno = int(input("Digite el incremento anual del terreno en porcentaje: "))
bajonAuto = int(input("Digite la devaluacion del auto anualmente  en porcentaje: "))

inc = (((precio * incTerreno)/100)*3)/2
dec = ((precio * bajonAuto)/100)*3

if inc > dec:
    print("No le solicito comprar el auto")
else:
    print("Si usted quiere podria comprar el auto tranquilamente!")
    
#ej6
pcT=int(input("¿Cuantas computadores desea llevar?: "))
valorPc = 11000

if (pcT >= 1 and pcT <= 4):
    cuenta = (pcT * valorPc)
    descuento = (cuenta * 0.10)
    totalC = (cuenta - descuento)
    print("Su total a pagar es: {}".format(totalC)) 
elif (pcT >= 5 and pcT <= 9):
    cuenta = (pcT * valorPc)
    descuento = (cuenta * 0.20)
    totalC = (cuenta - descuento)
    print("Su total a pagar es: {}".format(totalC)) 
elif (pcT > 10):
    cuenta = (pcT * valorPc)
    descuento = (cuenta * 0.40)
    totalC = (cuenta - descuento)
    print("Su total a pagar es: {}".format(totalC)) 
else:
   print("Digite una cantidad de computadores valida!")
   
#ej7
precioA=int(input("Digite el precio del aparato: "))
marca=(input("¿Que marca es su aparato?: "))

if (precioA >= 1 and precioA <= 1999):
    iva = (precioA * 0.16)
    totalP = (precioA + iva)
    print("Su total a pagar es: {}".format(totalP)) 
elif (precioA >= 2000 and marca == "nosy" or marca == "Nosy" or marca == "NOSY"):
    iva = (precioA * 0.16)
    descuento = (precioA * 0.10)
    descuentoN = (precioA * 0.05)
    totalP = (precioA + iva - descuento - descuentoN)
    print("Su total a pagar es: {}".format(totalP)) 
elif (precioA >= 2000):
    iva = (precioA * 0.16)
    descuento = (precioA * 0.10)
    totalP = (precioA + iva - descuento)
    print("Su total a pagar es: {}".format(totalP)) 
else:
   print("Digite una cantidad de computadores valida!")
   
#ej8
montoT=int(input("Digite el monto total de la compra: "))

if (montoT >= 500000):
    inversionP = (montoT * 0.55)
    prestamo = (montoT * 0.30)
    credito = (montoT * 0.15)
    intereses = (credito * 0.20)
    print("La inversion de la empresa sera de: {}".format(inversionP)) 
    print("El prestamo solicitado sera de: {}".format(prestamo)) 
    print("El valor del credito sera de: {}".format(credito)) 
    print("Los intereses tendran un total de: {}".format(intereses)) 
elif (montoT <= 499999):
    inversionP = (montoT * 0.70)
    credito = (montoT * 0.30)
    intereses = (credito * 0.20)
    print("La inversion de la empresa sera de: {}".format(inversionP)) 
    print("El valor del credito sera de: {}".format(credito)) 
    print("Los intereses tendran un total de: {}".format(intereses)) 
