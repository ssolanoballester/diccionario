#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import ConfigParser
import sys

#https://wiki.python.org/moin/ConfigParserExamples

ficheroCuestionario=os.getcwd() + "/" "config.ini"

def menu(prompt, choices):
    os.system('clear')
    print '\n\n{0}\n'.format(prompt)
    #print '\n\n\n'.format(prompt)
    count = len(choices)
    for i in range(count):
        print '({0}) {1}'.format(i + 1, choices[i])
    response = 0
    while response < 1 or response > count:
        response = raw_input('    Type a number (1-{0}): '.format(count))
        if response.isdigit():
            response = int(response)
        else:
            response = 0
    return response

def buy(stockamount, bondamount):
    response = menu('What to buy?', ['Stocks', 'Bonds', 'Nevermind'])
    # Do something

def sell(stockamount, bondamount):
    response = menu('What to sell?', ['Stocks', 'Bonds', 'Nevermind'])
    # Do something

def cambiofichero():
        #Solicitar la ruta del nuevo fichero
        newfile=str(raw_input("indique la ruta completa del nuevo fichero: \n > "))
        #Comprobar que existe y si no existe volver al menu (previo pulse una tecla para continuar)
        if os.path.dirname(fichero) and os.path.basename(fichero) :
            ficheroCuestionario=newfile
            print "El nuevo fichero es: " + ficheroCuestionario
        else:
            print "El fichero no existe y por tanto no será modificado"
            inp=raw_input("Pulse Enter para continuar...")

def crearNuevoFichero():
        #response = menu('¿prueba?', ['Stocks', 'Bonds', 'Nevermind'])
        fichero=str(raw_input("indique la ruta completa del nuevo fichero: \n > "))
        # Habría que comprobar que la ruta y fichero del nuevo fichero
        if os.path.dirname(fichero) and os.path.basename(fichero)=False :
            print "El fichero se creará con el nombre:  " + fichero
            ficheroCuestionario=os.getcwd() + "/" + fichero
        elif os.path.dirname(fichero)=False and os.path.basename(fichero) :
            sys.exit("el directorio de creación del fichero no existe. FIN")
        else
            if os.path.dirname(fichero) and os.path.basename(fichero) :
                sys.exit("El fichero ya existe. FIN")

def modificarfichero():
    #Crear una nueva seccion
    #Modificar una existente (estas dos opciones podrían pertenecer al menu)

    #try catch Para ver si puede abrir el fichero

    #Pedir una palabra

    #Pedir el significado

    #Insertar la palabra y el significado al final del fichero



# ======================================================================
# Main program starts here
# ======================================================================
stockamount=10000
bondamount=10000

main_menu_response = 0
while main_menu_response != 4:
    main_menu_response = menu('Que quieres hacer?', ['Crear nuevo fichero', 'Modificar fichero', 'Cambiar de fichero' ,'End'])
    if main_menu_response == 1:
        crearNuevoFichero()
        #buy(stockamount, bondamount)
    elif main_menu_response == 2:
        sell(stockamount, bondamount)
    elif main_menu_response == 3:
        cambiofichero()
