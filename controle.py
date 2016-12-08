import time
from palavra import *
from lista import Lista

class Controle:
    def __init__(self):
        self.numeroTermos = 0
        self.dadosCarregados = True
        self.tempoBusca = float()
    
    def __apagarTermos(self):
        pass

    def carregarDados(self,filename):
        pass

    def getTempoBusca(self):
        pass

    def find(self, prefixo, qtd):
        pass

class Trie(Controle):
    class Node:
        def __init__(self, char=None, weight=None):
            self.char, self.weight = char, weight
            self.left, self.down, self.right = None, None, None
            
        def __str__(self):
            return self.char

        def __repr__(self):
            return self.__str__()

    def __init__(self):
        Controle.__init__(self)
        self.root = None

    def __apagarTermos(self):
        self.root = None
        self.numeroTermos = 0
        self.dadosCarregados = False

    def getTempoBusca(self):
        return "%.5f" % self.tempoBusca

    def insert(self,word,weight,node):
        '''Insere nova string na trie.'''
        if not node:
            if not self.root:
                self.root = node = Trie.Node(word[0])
            else: node = Trie.Node(word[0])

        if word[0] > node.char:
            node.right = self.insert(word,weight,node.right)
        elif word[0] < node.char:
            node.left = self.insert(word,weight,node.left)
        else:
            if len(word) > 1:
                node.down = self.insert(word[1:],weight,node.down)
            else:
                node.weight = weight
        return node

    def __getByPrefix(self, prefix, node, v=[], skipFirst=True):
        ''' Retorna um vetor de Palavras com dado prefixo. '''
        if node is None:
            return []

        if node.down != None:
            if node.down.weight != None:
                v += [Palavra(prefix+node.down.char, node.down.weight)]
            self.__getByPrefix(prefix+node.down.char, node.down, v, False)
        if not skipFirst:
            if node.left != None:
                if node.left.weight != None:
                    v += [Palavra(prefix[:-1]+node.left.char, node.left.weight)]
                self.__getByPrefix(prefix[:-1]+node.left.char, node.left, v, False)

            if node.right != None:
                if node.right.weight != None:
                    v += [Palavra(prefix[:-1]+node.right.char, node.right.weight)]
                self.__getByPrefix(prefix[:-1]+node.right.char, node.right, v, False)
        return v

    def search(self,prefix):
        ''' Procura pelo prefixo na trie. '''
        atual = pai = self.root
        i = 0
        while atual is not None and i < len(prefix): # nao None
            if prefix[i] == atual.char:
                if i == len(prefix)-1:
                    if atual.weight != None: # caso o prefixo seja a palavra inteira
                        return [Palavra(prefix, atual.weight)] + self.__getByPrefix(prefix, atual, [])
                    else: return self.__getByPrefix(prefix, atual, [])
                atual = atual.down
                i+=1
            elif prefix[i] > atual.char:
                atual = atual.right
            else: atual = atual.left
        return

    def carregarDados(self,filename):
        if self.dadosCarregados:
            self.__apagarTermos()

        file = open(filename, 'r')
        for line in file.readlines()[1:]:
            dados = line.split()
            # somente se a linha não for vazia
            if dados != []:
                self.insert(' '.join(dados[1:]), int(dados[0]), self.root)
                self.numeroTermos += 1

        self.dadosCarregados = True
        file.close()

    def find(self, prefixo, qtd):
        t1 = time.time()
        resultados = self.search(prefixo)
        if resultados is None:
            return 'Nenhum resultado'
        sugestoes = Lista()
        for item in resultados:
            sugestoes.inserirOrdenado(item, comparaPorPeso)
            #se a lista de sugestoes passar a qtd, remove ultimo
            if sugestoes.size() > qtd:
                sugestoes.removerFim()
        t2 = time.time()
        self.tempoBusca = t2 - t1
        return sugestoes

class BSearch(Controle):
    def __init__(self):
        Controle.__init__(self)
        self.termos = list()
    
    def __apagarTermos(self):
        self.termos = []
        self.numeroTermos = 0
        self.dadosCarregados = False

    def getTempoBusca(self):
        return "%.5f" % self.tempoBusca
    
    def __firstIndexOf(self, prefixo):
        ''' Retorna o indice da primeira ocorrencia
            do prefixo no vetor de termos. '''
        inicio = 0
        fim = self.numeroTermos - 1
        while fim > inicio:
            meio = (inicio + fim) // 2
            cmp = comparaPorPrefixo(self.termos[meio], prefixo)
            if cmp > 0: # a palavra do meio vem depois do prefixo
                fim = meio - 1
            elif cmp < 0: # a palavra do meio vem antes do prefixo
                inicio = meio + 1
            else: # a palavra contem o prefixo
                fim = meio
        return inicio

    def __lastIndexOf(self, prefixo):
        ''' Retorna o indice da ultima ocorrencia
            do prefixo no vetor de termos. '''
        inicio = 0
        fim = self.numeroTermos - 1
        while fim >= inicio:
            meio = (inicio + fim) // 2
            if comparaPorPrefixo(self.termos[meio], prefixo) > 0: # a palavra do meio vem depois do prefixo
                fim = meio - 1
            else: # a palavra do meio vem antes ou contem o prefixo
                inicio = meio + 1
        return fim

    def carregarDados(self,filename):
        if self.dadosCarregados:
            self.__apagarTermos()

        file = open(filename, 'r')
        for line in file.readlines()[1:]:
            dados = line.split()
            # somente se a linha não for vazia
            if dados != []:
                self.termos.append(Palavra(' '.join(dados[1:]), int(dados[0])))
                self.numeroTermos += 1

        self.termos.sort()
        self.dadosCarregados = True
        file.close()

    def find(self, prefixo, qtd):
        t1 = time.time()
        f, l = self.__firstIndexOf(prefixo), self.__lastIndexOf(prefixo)
        # print("{0}: indice {1} a {2}".format(prefixo,f,l))

        # quando f > l ou f == l (e nao achou nada) mas nao ha prefixo
        if (f > l) or (f == l and comparaPorPrefixo(self.termos[f], prefixo) != 0):
            return 'Nenhum resultado'

        sugestoes = Lista()
        for item in self.termos[f:l+1]:
            sugestoes.inserirOrdenado(item, comparaPorPeso)
            #se a lista de sugestoes passar a qtd, remove ultimo
            if sugestoes.size() > qtd:
                sugestoes.removerFim()
        t2 = time.time()
        self.tempoBusca = t2-t1
        return sugestoes
