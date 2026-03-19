import random
from abc import ABC, abstractmethod

'''
    Abstração
    Classe base abstrata
'''

class Jogo(ABC):
    
    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def jogar(self):
        pass


'''
    Herança
    Classe que herda classe Jogo
'''

class JogoAdivinhação(Jogo):

    '''
        Encapsulamento
        atributos privados
    '''

    def __init__(self):
        self.__numero_secreto = random.randint(1, 100)
        self.__tentativas = 0
        self.__limite = 10


    def iniciar(self):
        print("Jogo da adivinhação")
        print("-------------------")
        print("Adivinhe o número entre 1 e 100")
        print("Você tem", self.__limite, "tentativas\n")  


    '''
        Polimorfismo
        implementação do método abstrato
    '''

    def jogar(self):  

        while self.__tentativas < self.__limite:
            
            try:
                palpite = int(input("Digite seu palpite: "))  
            except:
                print("Digite apenas números!")
                continue
            
            self.__tentativas += 1
            
            if palpite == self.__numero_secreto:
                print("\nParabéns! Você acertou!")
                print("Tentativas usadas:", self.__tentativas)  
                return
            
            elif palpite < self.__numero_secreto:  
                print("O número secreto é MAIOR\n")

            else:
                print("O número secreto é MENOR")
            
        print("\nSuas tentativas acabaram!")
        print("O número secreto era:", self.__numero_secreto)


'''
    Polimorfismo
    função que executa qualquer jogo
'''

def executar_jogo(jogo: Jogo):  
    jogo.iniciar()
    jogo.jogar()


'''
    Programa Principal
'''

jogo = JogoAdivinhação()
executar_jogo(jogo)