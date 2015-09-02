#!/usr/bin/python3
# -*- utf-8-*-

from math import sqrt

print('Bienvenido\nIngrese por favor los valores requeridos\nrecuerde hacerlo en formato de numeros con punto decimal')
Vin = float(input('\nIngrese el Voltaje de Entrada:\n'))
Vout = float(input('\nIngrese el Voltaje de Salida deseado:\n'))
At = float(input('\nIngrese el valor del area transversal del nucleo:\n'))
print('Calculando... \nPorfavor Espere...\n')
Pmax = sqrt(At)
IoM = Pmax/Vout
IiM = Pmax/Vin
print('\nIout=',IoM,'Amp','\nIin=',IiM,'Amp','\nPmax=',Pmax,'Watts')
