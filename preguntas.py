"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
def leer_archivo():
    with open('data.csv', encoding='utf-8') as file:
        content = file.readlines()
    registros=[]
    for renglon in content:
        registros.append(renglon.split("\t"))
    return registros

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    registros=leer_archivo()
    pos_2=[]
    for i in registros:
        pos_2.append(int(i[1]))
    total=sum(pos_2)
    return total

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    registros=leer_archivo()
    
    diccionario = {}
    for key in registros:
        if key[0] not in diccionario.keys():  
            diccionario[key[0]] = 1   
        else:
            diccionario[key[0]]+=1
    tuplas = [(key, value) for key, value in diccionario.items()]
    return sorted(tuplas)

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    registros=leer_archivo()
    
    diccionario = {}
    for i in registros:
        if i[0] not in diccionario.keys():  
            diccionario[i[0]] = int(i[1]) 
        else:
            diccionario[i[0]]+=int(i[1])
    tuplas = [(key, value) for key, value in diccionario.items()]
    return sorted(tuplas)

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    registros=leer_archivo()

    diccionario = {}
    for i in registros:
        mes=i[2].split("-")[1]
        if mes not in diccionario.keys():  
            diccionario[mes] = 1 
        else:
            diccionario[mes]+=1
    tuplas = [(key, value) for key, value in diccionario.items()]
    return sorted(tuplas)


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    registros=leer_archivo()
    
    diccionario = {}
    for i in registros:
        if i[0] not in diccionario.keys():  
            diccionario[i[0]] = [int(i[1]),int(i[1])] 
        else:
            if diccionario[i[0]][0] < int(i[1]):
                diccionario[i[0]][0] = int(i[1])
            if diccionario[i[0]][1] > int(i[1]):
                diccionario[i[0]][1] = int(i[1])
    tuplas = [(key, max(value), min(value)) for key, value in diccionario.items()]
    return sorted(tuplas)

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    registros=leer_archivo()
    
    diccionario = {}
    for i in registros:
        pareja=i[4].split(",")
        for llave in pareja:
            llave,valor = llave.split(":")
            if llave not in diccionario.keys():  
                diccionario[llave] = [int(valor),int(valor)]
            else:
                if diccionario[llave][0] > int(valor):
                    diccionario[llave][0] = int(valor)
                if diccionario[llave][1] < int(valor):
                    diccionario[llave][1] = int(valor)

    tuplas = [(key, min(value), max(value)) for key, value in diccionario.items()]
    return sorted(tuplas)

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    registros=leer_archivo()
    diccionario={}
    for i in registros:
        if int(i[1]) not in diccionario.keys():
            diccionario[int(i[1])] = [i[0]]
        else:
            diccionario[int(i[1])].append(i[0])

    tuplas = [(key, value) for key, value in diccionario.items()]
    return sorted(tuplas)

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    registros=leer_archivo()
    diccionario={}
    for i in registros:
        if int(i[1]) not in diccionario.keys():
            diccionario[int(i[1])] = [i[0]]
        else:
            if i[0] not in diccionario[int(i[1])]:
                diccionario[int(i[1])].append(i[0])
                diccionario[int(i[1])].sort()

    tuplas = [(key, value) for key, value in diccionario.items()]
    return sorted(tuplas)


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    registros=leer_archivo()
    
    diccionario = {}
    for i in registros:
        sin_coma=i[4].split(",")
        sin_punto=[i.split(":") for i in sin_coma]
        for llave in sin_punto:
            if llave[0] not in diccionario.keys():
                diccionario[llave[0]] = 1
            else:
                diccionario[llave[0]] += 1
    return dict(sorted(diccionario.items()))

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    registros=leer_archivo()
    
    lista = []
    for i in registros: 
        elem_4= i[3].split(",")
        elem_5= i[4].split(",")
        lista.append((i[0], len(elem_4), len(elem_5)))
    return lista

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    registros=leer_archivo()
    
    diccionario = {}
    for i in registros:
        sin_coma=i[3].split(",")
        for y in sin_coma:
            if y not in diccionario.keys():
                diccionario[y] = int(i[1])
            else:
                diccionario[y] += int(i[1])
    return dict(sorted(diccionario.items()))

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    registros=leer_archivo()
    diccionario = {}
    for i in registros:
        sin_coma=i[4].split(",")
        sin_punto=[i.split(":") for i in sin_coma]
        for x in sin_punto:
            if i[0] not in diccionario.keys():  
                diccionario[i[0]] = int(x[1])
            else:
                diccionario[i[0]] += int(x[1])
    return dict(sorted(diccionario.items()))
