from palavra import *
from lista import Lista

class Controle:
    def __init__(self):
        self.numeroTermos = 0
        self.termos = list()
        self.dadosCarregados = True
    
    def __apagarTermos(self):
        self.termos = []
        self.numeroTermos = 0
        self.dadosCarregados = False
    
    #Pronto
    def __firstIndexOf(self, prefixo):
        inicio = 0
        fim = self.numeroTermos-1                       
        pos = -1
        while inicio < fim:
            pos = (inicio + fim)//2
            if comparaPorPrefixo(self.termos[pos], prefixo) == 0:
                fim = pos
            elif comparaPorPrefixo(self.termos[pos], prefixo) == 1:
                fim = pos-1
            else:
                inicio=pos+1
        return pos
    
    #Pronto
    def __lastIndexOf(self, prefixo):
        inicio = 0
        fim = self.numeroTermos-1                       
        pos = (inicio + fim)//2
        while inicio <= fim:
            print("inicio: {0}\nmeio: {1}\nfim: {2}".format(inicio, pos, fim))
            if comparaPorPrefixo(self.termos[pos], prefixo) == 0 :
                if pos == fim:
                    return pos
                    break
                elif comparaPorPrefixo(self.termos[pos+1], prefixo) == 1 :
                    return pos
                    break
                else:
                    pos = pos +1
            elif comparaPorPrefixo(self.termos[pos], prefixo) == 1:
                fim = pos
                pos = (inicio + fim)//2
            elif comparaPorPrefixo(self.termos[pos], prefixo) == -1:
                inicio = pos
                pos = (inicio + fim)//2

    #Pronto 
    def carregarDados(self,filename):
        if self.dadosCarregados:
            self.__apagarTermos()

        f = open(filename, 'r', encoding="utf-8")
        for linha in f.readlines():
            termo = linha.split()
            cpeso = int(termo.pop(0))

            if len(termo) != 0:
                aux = " ".join(termo)
                self.termos.append(Palavra(aux,cpeso))
                self.numeroTermos += 1 

        f.close()
        self.termos.sort() 
        self.dadosCarregados = True        
        
    def find(self, prefixo, qtd):
        first = self.__firstIndexOf(prefixo)
        last = self.__lastIndexOf(prefixo)
        termos =  self.termos[first:last]

        selecionadas = Lista()
        for item in termos:         
            selecionadas.inserirOrdenado(item, comparaPorPeso)  
            if selecionadas.size() == qtd:
                selecionadas.removerFim()
                

        return selecionadas

    def fl(self, prefixo):
        return self.__firstIndexOf(prefixo)

a = Controle()
a.carregarDados('cities.txt')
