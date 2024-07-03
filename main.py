import os.path
import utils
path = 'gastos.csv'

if not os.path.isfile(path):
    file = open('gastos.csv', 'w')
    file.close()
else:
    print('ya existe')
    pass

gastos = []

while True:
    #el programa corre mienstras no quiera salir
    
    print("""Que quieres hacer? ingresa el numero de la operacion que desees ejecutar 
                   1.- registrar un gasto
                   2.- buscar gastos por rango de fechas
                   3.- buscar gastos por categoria
                   4.- ver las estadisticas totales de los gastos
                   5.- actualizar un gasto
                   6.- eliminar un gasto\n""")
    opcion = input('operacion a realizar')
    if opcion == '1':
        pass
    elif opcion == '2':
        pass
    elif opcion == '3':
        pass
    elif opcion == '4':
        pass
    elif opcion == '5':
        pass
    elif opcion == '6':
        break