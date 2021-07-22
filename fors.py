lista = ('I', 'V', 'X')

for ix in range(len(lista)):
    print("{} - {}".format(ix, lista[ix]))

for ix, caracter in enumerate(lista):
    print("{} - {}".format(ix, caracter))

for tupla in enumerate(lista):
    print("{} - {}".format(tupla[0], tupla[1]))
