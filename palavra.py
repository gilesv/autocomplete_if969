class Palavra:
    def __init__(self,termo="",peso=-1):
        self.termo = termo
        self.peso = peso
    
    #Pronto
    def __lt__(self,other):
        minuscula = self.termo
        minusculaot = other.termo
        return ((minuscula.lower())<(minusculaot.lower()))
    
    def __str__(self):
        return "{0}, {1}".format(self.termo,self.peso)
    
    def __repr__(self):
        return self.__str__()

#Pronto      
def comparaPorPrefixo(palavra, prefixo):
    tamanho = len(prefixo)
    if prefixo < palavra.termo[:tamanho]:
        return 1
    elif prefixo == palavra.termo[:tamanho]:
        return 0
    else: 
        return -1
    

#Pronto
def comparaPorPeso(palavra1, palavra2):

    if ((palavra1.peso) < (palavra2.peso)):
        return 1
    elif ((palavra1.peso) == (palavra2.peso)):
        return 0
    else:
        return -1
