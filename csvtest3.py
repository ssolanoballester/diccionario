#To be able to read csv formated files, we will first have to import the
#csv module.
import csv
from random import randrange
#with open('csvtest.csv', 'rb') as f:
#    reader = csv.reader(f)
#    for row in reader:
#        print row


ifile  = open('phrasal3.csv', 'rb')
reader = csv.reader(ifile,delimiter=';')

rownum = 0
lista=[]
listatemp=[]

for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
    else:
        colnum = 0
        #print type(row)
        #print row
        #print colnum
        mi_tupla=(row[0],row[1],row[2])
        #var=raw_input("Presiona enter para continuar")
        #for col in row:
        #    listatemp.append(col)
            #print '%s: %s' % (header[colnum], col)
            #colnum += 1
        #lista.append(listatemp)
        lista.append(mi_tupla)



#    print lista
#    var=raw_input("Presiona enter para continuar")
#    print
#    print
    rownum += 1

#print lista[1][2]
ifile.close()

#print "printando lista antes del segundo bucle"
#print len(lista)
#print lista[17]
#var=raw_input("Presiona enter para continuar")

while ((len(lista))>0):
    random_index = randrange(0,len(lista))
    #print "Indice random %s" % random_index
    #print "tipo de random_index: %s" % type(random_index)
    #print type(lista)
    #print lista[random_index]
    #print lista[random_index]
    #print lista[17]
    print "phrasal verb:      %s" % lista[random_index][0]
    var=raw_input("")
    print "definition  :      %s" % lista[random_index][1]
    var=raw_input("")
    print "example     :      %s" % lista[random_index][2]
    print
    #var=raw_input("")
    #print lista[random_index][1]
    #print lista[random_index]
    #Me falta quitar el elemento seleccionado de la lista
    print
    print
    lista.remove(lista[random_index])


