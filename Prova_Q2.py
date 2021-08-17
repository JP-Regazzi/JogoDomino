class Dominos: # Exemplo de entrada: [[1,2],[5,6],[3,1],[6,4]] -> cada lista menor é uma peça!
ça!
    def __init__(self, lista):
        self.lista = lista
        self.mesa = []
        if self.mesa == []:
            self.n1, self.n2 = lista[0]

    def compra(self):
        try:
            if self.lista == []:    # Se a lista de pecas para comprar estiver vazia, o codigo da um value error
                a,b = [1,2,3,4,5]
            comprado = self.lista[0]
            self.lista.pop(0)
        except ValueError:
            print('Não há mais peças disponíveis')
            raise
        return comprado

    def coloca(self, peca, extremidade):
        if self.mesa == []:       # Se a mesa estiver vazia
            self.mesa.append(peca)
            self.n1, self.n2 = peca
            return True
        elif self.n1 == peca[0] and extremidade == 0:   # Se o primeiro numero da peca se encaixar "em cima"
            self.n1 = peca[1]
            self.mesa.insert(0,tuple(reversed(peca)))
            return True
        elif self.n1 == peca[1] and extremidade == 0:  # Se o segundo numero da peca se encaixar "em cima"
            self.n1 = peca[0]
            self.mesa.insert(0, peca)
            return True
        elif self.n2 == peca[0] and extremidade == 1:  # Se o primeiro numero da peca se encaixar "embaixo"
            self.n2 = peca[1]
            self.mesa.append(peca)
            return True
        elif self.n2 == peca[1] and extremidade == 1:  # Se o segundo numero da peca se encaixar "embaixo"
            self.n2 = peca[0]
            self.mesa.append(tuple(reversed(peca)))
            return True
        else:
            return False

    def imprime(self):  # Nao deu tempo de eu formatar a impressao
        resultado = ''
        pular = True
        for i, tupla in enumerate(self.mesa):
            if i == (0 or 2 or 4 or 6):
                pular = True
            if i == (1 or 3 or 5 or 7):
                pular = False
            for caracter in tupla:
                if pular:
                    resultado += f'{caracter}\n'

                else:
                    resultado += f'{caracter}'
        print(resultado)

lista_das_pecas = eval(input())
d = Dominos(lista_das_pecas)
for x in range(len(lista_das_pecas)):
    p = d.compra()
    c1 = d.coloca(p, 0)
    if not c1:
        d.coloca(p, 1)


d.imprime()

