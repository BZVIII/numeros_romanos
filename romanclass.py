class RomanNumber():
    def __init__(self, valor):

        if isinstance(valor, int):
            self.valor = valor
            self.cadena = self.a_romano(valor)

    def validar(self, n):
        if not isinstance(n, int):
            raise ValueError("{} debe ser un entero".format(n))

        if n < 0 or n > 3999:
            raise ValueError("{} debe estar entre 0 y 3999".format(n))


    def a_romano(self):
        self.validar(self.valor)
        c = "{:04d}".format(n)
        
        unidades = int(c[-1])
        decenas = int(c[-2])
        centenas = int(c[-3])
        millares = int(c[-4])

        return simbolos['millares'][millares] + simbolos['centenas'][centenas] + simbolos['decenas'][decenas] + simbolos['unidades'][unidades]
