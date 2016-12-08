from mainwindow import Ui_MainWindow
from controle import *

class GUI(Ui_MainWindow):
    def __init__(self):
        self.controle = Trie()

    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)
        self.inputFileText.textChanged.connect(self.inputFileChanged)
        self.botaoOK.clicked.connect(self.carregarDados)
        self.qtdPalavraText.textChanged.connect(self.autocompletar)
        self.palavraText.textChanged.connect(self.autocompletar)
        self.radioTrie.toggled.connect(self.useTrie)
        self.radioBin.toggled.connect(self.useBin)

    def inputFileChanged(self):
        self.botaoOK.setEnabled(self.inputFileText.text().strip() != "")

    def useTrie(self):
    	self.controle = Trie()

    def useBin(self):
    	self.controle = BSearch()
    
    def carregarDados(self):
        self.controle.carregarDados(self.inputFileText.text())
        self.palavraText.setEnabled(True)
    
    def autocompletar(self):
        texto = self.palavraText.text()
        qtd = self.qtdPalavraText.text()
        if texto != "" and qtd != "":
            lista = self.controle.find(texto,int(qtd))
            self.outputText.setText(str(lista))
            self.tempoLabel.setText("Tempo de busca: {0} segundos".format(self.controle.getTempoBusca()))
        else:
            self.outputText.clear()
