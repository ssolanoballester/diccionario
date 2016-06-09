#/usr/bin/python
# -*- coding: utf-8 -*-
import json, os
#from ConfigParser import SafeConfigParser
#import ConfigParser
try:
            from configparser import ConfigParser
except ImportError:
            from ConfigParser import ConfigParser  # ver. < 3.0

##################################################
# Important url's
# https://pymotw.com/2/ConfigParser/
# https://wiki.python.org/moin/ConfigParserExamples
#
#
#
#
##################################################

parser = ConfigParser()
#parser = ConfigParser.ConfigParser()
#parser = SafeConfigParser()
#parser.readfp(open('palabras.ini','w'))
parser.read('palabras.ini')
#cfgfile = open("ejemplo1.ini",'a')
#parser.readfp = open("palabras.ini",'a')
# add the settings to the structure of the file, and lets write it out...
#parser.read(config)
#parser.read(cfgfile)
#parser.read('palabras.ini')
lista_secciones=[]

stockamount=10000
bondamount=10000
ficheroCuestionario=os.getcwd() + "/" "config.ini"

# ======================================================================
# Main program starts here
# ======================================================================

def main():
    #Creamos la variable que recoge la opcion del menu
    main_menu_response = 0
    while main_menu_response != 6:
        #Llamamos al menu para que pinte las opciones
        main_menu_response = menu('Que quieres hacer?', ['Crear nueva seccion',
                                                         'Eliminar seccion',
                                                         'Modificar seccion',
                                                         'Listar secciones',
                                                         'Lanzar encuesta',
                                                         'Finalizar'])
        #print main_menu_response
        #p=raw_input("comienza el if")
        if main_menu_response == 1:
            #Añadimos una sección
            crear_Seccion()
        elif main_menu_response == 2:
            #Borramos una sección
            print "pasa por opcion 2"
            eliminar_Seccion()
        elif main_menu_response == 3:
            #Modificamos una sección (¿reescritura completa?)
            modificar_seccion()
        elif main_menu_response == 4:
            listar_secciones(1)
        elif main_menu_response == 5:
            lanzar_encuesta()

    # save to a file
    #with open('palabras_update.ini', 'w') as configfile:
    with open('palabras.ini', 'w') as configfile:
        parser.write(configfile)

#    parser.write.close()



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
            #print type(response)
            #print response
            #p=raw_input("paso por if is digit")
            response = int(response)
        else:
            #p=raw_input("paso por elseif is digit")
            response = 0
    return response

#######################################################
# Crear seccion 
#######################################################
def crear_Seccion():
    s=raw_input("Introducta el nombre de la seccion:  ")
    parser.add_section(s)
    res=""
    while res!=exit :
        wword=raw_input("Escriba el nombre de la palabra a añadir o escriba \
exit si ya ha terminado:  ")
        wmean=raw_input("Escriba el significado de palabra añadida o \
escriba exit si ya ha terminado:  ")
        if (wword == "exit") or (wmean == "exit"):
            return
        else:
            parser.set(s,wword,wmean)
    parser.write('palabras.ini')
    parser.write(cfgfile)
    cfgfile.close()
    #zz=raw_input("Se acaba de escribir el fichero (en teoria)")
    return


def eliminar_Seccion():
    listar_secciones()
    n_seccion=raw_input("Introducta el numero de la seccion a eliminar:  ")
    #Aqui haria falta hacer un try - catch por si se teclea un numero fuera del
    #rango de la lista de secciones
    d_seccion=parser.sections()
    #s_seccion=d_seccion[(int(n_seccion))-1]
    #print s_seccion
    #a234=raw_input("Pulse ENTER para continuar")
    #Meter en una lista las secciones

    #
    if parser.has_section(d_seccion[(int(n_seccion))-1]):
        #parser.remove_section(d_seccion)
        parser.remove_section(d_seccion[(int(n_seccion))-1])
    else:
        os.system('clear')
        print '\n\n{0}\n'.format("La seccion no existe")


def listar_secciones(tecla):
    #yx=raw_input("Pasa por listar seccciones  ")
    secciones=parser.sections()
    count2=len(secciones)
    for i in range(count2):
        print '({0}) {1}'.format(i + 1, secciones[i])
    if tecla==1 :
        a234=raw_input("Pulse ENTER para continuar")


def modificar_seccion():
    listar_secciones()
    #pass

## Seccion que lista las secciones y devuelve el valor de la seccion escogida
#def lista_secciones():
#    secciones=parser.sections()
#    count2=len(secciones)
#    for i in range(count2):
#        print '({0}) {1}'.format(i + 1, secciones[i])
#    print
#    res=raw_input("Elige la opcion  ")
#    if tecla==1 :
#        a234=raw_input("Pulse ENTER para continuar")


#TO-DO List
#Mirar que la última respuesta no desapareza de pantalla
#Hacer el computo total de puntuacion
#Hacer la encuesta de forma aleatoria
#Escoger una seccion de forma aleatoria
def lanzar_encuesta():
    #seccion_escogida=lista_secciones()
    listar_secciones(0)
    res=raw_input("Elige la opcion sobre la cual quieres que se pregunte ")
    #secciones=(parser.sections())[int(res))-1]
    secciones=parser.sections()
    seccion_escogida=secciones[int(res)-1]
    #print secciones
    #print seccion_escogida
    #a234=raw_input("Pulse ENTER para continuar")

    #[(int(n_seccion))-1]

    #seccion_escogida=listar_secciones()
    #llamar a la funcion de preguntar_palabras(seccion_escogida)
    #Recorrer un diccionario mostrando clave o valor y pregunta
    for name, value in parser.items(seccion_escogida):
        w_palabra=raw_input("The word is:  " + name + "  su significado es:  ")
        #print type(w_palabra)
        #print w_palabra
        #print
        #type(parser.get(seccion_escogida, name))
        #print (parser.get(seccion_escogida,name))
        if w_palabra == (parser.get(seccion_escogida, name)):
            print "respuesta correcta"
            print("Efectivamente la respuesta es:  ")
            print(parser.get(seccion_escogida,name))
            #Aqui se puede poner un contador para que cuente las respuestas
        else:
            print "respuesta_incorrecta"
            print "La respuesta correcta es: "
            print(parser.get(seccion_escogida,name))



def ver_secciones_y_opciones():
    for section_name in parser.sections():
        print 'Section:', section_name
        print 'Options:', parser.options(section_name)
    for name, value in parser.items(section_name):
        print '  %s = %s' % (name, value)
    print



def nombre_funcion():
    pass


if __name__ == "__main__":
    main()
