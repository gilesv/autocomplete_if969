class No:
    def __init__(self,item=None,ant=None,prox=None):
        self.item = item
        self.ant = ant
        self.prox = prox
    
class Lista:

    def __init__(self):
        self.primeiro = self.ultimo = No()
        self.tamanho = 0
    
    def size(self):
        return self.tamanho

    def vazio(self):
        return self.primeiro == None

    def inserir(self, item):
        no = No(item, self.ultimo, None)
        self.ultimo.prox = no
        self.ultimo = no
        self.tamanho +=1

        
    #Pronto
    def inserirOrdenado(self, item, cmp):    
        '''
        Insere ordenado conforme funcao de comparacao passada como parametro.
        cmp: funcao de comparacao que retorna <0, 0 ou >0 se primeiro valor
            for menor, igual ou maior que o segundo valor 
        '''
        if self.vazio():
            self.inserir(item)

            
        anterior = self.primeiro
        atual = anterior.prox

                   
        while ((not( atual is None)) and (cmp(item, atual.item) <= 0)):
            anterior = atual
            atual = anterior.prox
        no = No(item,anterior,atual)    
        anterior.prox = no
        self.tamanho +=1
        if atual is None:
            self.ultimo = no
    
        
        
    #Pronto   
    def removerFim(self):
        if (self.vazio()):
            return None
        ultimo = self.ultimo
        self.ultimo = ultimo.ant
        self.ultimo.prox = None
        ultimo.ant = None
        self.tamanho -= 1
        
    def __str__(self):
        total = ''
        atual = self.primeiro.prox
        while atual != None:
            total += atual.item.termo + '\n'
            atual = atual.prox
        return total
    
    def __repr__(self):
        return str(self)


