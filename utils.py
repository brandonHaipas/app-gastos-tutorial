from datetime import datetime
def ingresar_gasto(descripcion, cat, fecha, monto, file):
    #handling usuario
    index = '0'
    gastos_lista = crear_lista_gastos(file)
    len_gasto = len(gastos_lista)
    if len_gasto>0:
        index = str(int(gastos_lista[len_gasto-1]['index'])+1)
        
    try:
        with open(file, 'a') as gastos:
            line = index + '\t' + descripcion +'\t' + cat +'\t'+ fecha + '\t'+ monto + '\n'
            gastos.write(line)
            print('texto guardado!')
    except Exception as e:
        print(f"Error : {e}")

def crear_lista_gastos(file):
    
    ret_value = []
    try:
        with open(file, 'r') as gastos:
            output = gastos.read()
            lines = output.split(sep='\n')
            gastos_list = []
            for line in lines:
                if line == '':
                    break
                
                line_list = line.split('\t')
                
                line_dict = {'index':line_list[0], 'descripcion':line_list[1], 'cat':line_list[2], 'fecha':datetime.strptime(line_list[3], '%d-%m-%Y'), 'costo':line_list[4]}

                gastos_list.append(line_dict)
            ret_value = gastos_list
            
    except Exception as e:
        print(f'Error: {e}')
    return ret_value
            
def buscar_por_fechas(file, fecha_inicio, fecha_final):
    gastos_filtrados = []
    lista_gastos = crear_lista_gastos(file)
    sorted_list = sorted(lista_gastos, key=lambda d: d['fecha'])
    start = datetime.strptime(fecha_inicio, '%d-%m-%Y')
    stop = datetime.strptime(fecha_final, '%d-%m-%Y')
    if stop < start:
        print('no existe este rango de fechas!')
        
    for i in sorted_list:
        if i['fecha'] >= start and  i['fecha']<=stop:
            gastos_filtrados.append(i)
        elif i['fecha']> stop:
            break
    return gastos_filtrados
        
def buscar_por_categoria(file, cat):
    lista_gastos = crear_lista_gastos(file)
    return [gasto for gasto in lista_gastos if gasto['cat'] == cat]
    
def gasto_a_string(gasto):
    llaves = gasto.keys()
    gasto_str = ''
    for i in llaves:
        if i == 'fecha':
            gasto_str += gasto[i].strftime('%d-%m-%Y') + '\t'
        else:
            gasto_str += (gasto[i] + '\t')
    return gasto_str 

def eliminar_gasto(index, file):
    num_index = int(index)
    lista_gastos = crear_lista_gastos(file)
    lista_gastos.pop(num_index)
    len_gastos = len(lista_gastos)
    for i in range(num_index, len_gastos):
        lista_gastos[i]['index'] = str(int(lista_gastos[i]['index']) - 1)
    try:
        with open(file, 'w') as gastos_file:
           gastos_string =  ""
           for elem in lista_gastos:
               gastos_string+= gasto_a_string(elem) + '\n'
           gastos_file.write(gastos_string)
    except Exception as e:
        print(f"Error {e}") 
        
def actualizar_gasto(index, descripcion, cat, fecha, monto, file):
    num_index = int(index)
    lista_gastos = crear_lista_gastos(file)
    lista_gastos[num_index] = {'index':index, 'descripcion':descripcion, 'cat':cat, 'fecha':datetime.strptime(fecha, '%d-%m-%Y'), 'costo':monto}
    try:
        with open(file, 'w') as gastos_file:
           gastos_string =  ""
           for elem in lista_gastos:
               gastos_string+= gasto_a_string(elem) + '\n'
           gastos_file.write(gastos_string)
    except Exception as e:
        print(f"Error {e}") 
        
def estadisticas_generales(file):
    lista_gastos = crear_lista_gastos(file)
    total_gastos = len(lista_gastos)
    categorias_raw = [gasto['cat'] for gasto in lista_gastos]
    categorias = list(set(categorias_raw))
    cat_dict = {}
    for cat in categorias:
        cat_dict[cat] = buscar_por_categoria(file, cat)