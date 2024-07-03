from datetime import datetime
def ingresar_gasto(descripcion, cat, fecha, monto, file):
    #handling usuario
    try:
        with open(file, 'a') as gastos:
            line = descripcion +'\t' + cat +'\t'+ fecha + '\t'+ monto + '\n'
            gastos.write(line)
            print('texto guardado!')
    except Exception as e:
        print(f"Error : {e}")

def crear_lista_gastos(file):
    
    ret_value = []
    try:
        with open('gastos.csv', 'r') as gastos:
            output = gastos.read()
            lines = output.split(sep='\n')
            gastos_list = []
            for line in lines:
                if line == '':
                    break
                line_list = line.split('\t')
                line_dict = {'descripcion':line_list[0], 'cat':line_list[1], 'fecha':datetime.strptime(line_list[2]), 'costo':line_list[3]}
                gastos_list.append(line_dict)
            ret_value = gastos_list
            
    except Exception as e:
        print(f'Error: {e}')
    return ret_value
            
def buscar_por_fechas(file, fecha_inicio, fecha_final):
    lista_gastos = crear_lista_gastos(file)
    sorted_list = sorted(lista_gastos, key=lambda d: d['fecha'])
    start = datetime.strptime(fecha_inicio)
    stop = datetime.strptime(fecha_final)