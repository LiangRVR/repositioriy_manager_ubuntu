"""
Para que el programa pueda ejercer cambios, es necesario ejecutarlo con permisos de administrador.

Requisitos:
1. Cada seccion de repositiorio a activar tiene q estar encerrado por una identificacion.
2. La identificacion de apertura tiene que tener la forma #repo_ seguido del nombre deseado.
3. La identificacion de cerrar la seccion tiene que ser igual que la de apertura con un "/", #/repo_

Ejemplos de una seccion:

#repo_casa
.
.
.
#/repo_casa

#repo_Hola
.
.
.
#/repo_Hola

"""

import re


def set_repo(data_repositorie, tag):
    """
    Selecionar determinada por sion de repositiorio atendiendo al identificador introducido.
    """
    set_repo = False
    for i, direcc in zip(range(len(data_repositorie)), data_repositorie):
        if ("#"+tag.lower()) == direcc.lower():
            set_repo = True
        if ("#/"+tag.lower()) == direcc.lower():
            set_repo = False

        if "deb http" in direcc:
            is_sharp = "#" in direcc
            if set_repo == True and is_sharp == True:
                data_repositorie[i] = direcc[1:]
            elif set_repo == False and is_sharp == False:
                data_repositorie[i] = "#" + direcc

    return data_repositorie


def read_file(dir):
    """
    Leer el fichero a trabajar y lista los identificadores de los repositorios
    """
    data_repo = []
    list_repo = {}
    cont = 1
    with open(dir, 'r') as file:
        for line in file:
            line = re.sub('\n', '', line)
            if "#repo_" in line:
                list_repo.setdefault(cont, line[1:])
                cont = cont + 1
            data_repo.append(line)
        file.close()
    return list_repo, data_repo


def write_file(dir, data_repo):
    """
    Escribir el fichero con los cambios sleccionados.
    """
    with open(dir, 'w+') as file:
        for line in data_repo:
            line = line + "\n"
            file.write(line)
        file.close()


#set_tag = input("Insert repository tag for activate it: ")
direction = "/etc/apt/sources.list"
list_repo, data = read_file(direction)

"""
deploy a list of tag's repo and give a chance to choise one of then
"""

while True:
    print("Select a tag to active it:")
    select="["
    for index, rep in zip(list_repo.keys(),list_repo.values()):
        print(f"({index}) {rep}")
        select = select + str(index) + " , "
    select= select[:-3]+"]: "
    set_tag = int(input(select))
    if list_repo.get(set_tag) != None:
        set_tag = list_repo[set_tag]
        break
    print("Wrong choise!!!. Try again")
    

write_file(direction, set_repo(data, set_tag))
print(f"\"{set_tag}\" was actived")