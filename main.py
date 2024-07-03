import os.path
from utils import *
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
                   6.- eliminar un gasto
                   7.- terminar el programa\n""")
    opcion = input('operacion a realizar: ')
    if opcion == '1':
        print("Ingrese los datos del registro a continuacion: \n")
        descripcion = input('Breve descripcion:\n')
        cat = input("categoria:\n")
        dia = input('dia:\n')
        mes = input('mes:\n')
        anho = input('año:\n')
        costo = input('costo:\n')
        
        fecha = '-'.join([dia,mes,anho])#dia-mes-anho
        ingresar_gasto(descripcion, cat , fecha , costo, 'gastos.csv')
        
    elif opcion == '2':
        print("A continuacion ingrese la fecha de inicio y la fecha de termino del periodo de gastos que quiere ver: \n")
        print('Fecha de inicio\n')
        dia_inicio = input('dia\n')
        mes_inicio = input('mes\n')
        anho_inicio = input('año\n')
        print('Fecha de termino\n')
        dia_termino = input('dia\n')
        mes_termino = input('mes\n')
        anho_termino = input('año\n')
        
        start = '-'.join([dia_inicio, mes_inicio, anho_inicio])
        stop = '-'.join([dia_termino, mes_termino, anho_termino])
        filtrados = buscar_por_fechas('gastos.csv', start, stop)
        for gasto in filtrados:
            print(gasto_a_string(gasto) + '\n')
    elif opcion == '3':
        pass
    elif opcion == '4':
        pass
    elif opcion == '5':
        pass
    elif opcion == '6':
        index = input("indice del gasto a eliminar: ")
        eliminar_gasto(index, 'gastos.csv')
    elif opcion == '7':
        break