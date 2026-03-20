import random
from abc import ABC, abstractmethod

'''
    Melhorias:
        inserir o nome do jogador,
        escolher nível de dificuldade,
        jogar o jogo de adivinhação,
        calcular pontuação,
        armazenar jogadores no ranking,
        exibir o ranking ordenado.
'''

# ===============================
# CLASSE ABSTRATA (ABSTRAÇÃO)
# ===============================
class Jogo(ABC):
    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def jogar(self):
        pass


# ===============================
# CLASSE JOGO DE ADIVINHAÇÃO
# ===============================
class JogoAdivinhacao(Jogo):

    def __init__(self, nome, dificuldade):
        # ===============================
        # ENCAPSULAMENTO (atributos privados)
        # ===============================
        self.__nome = nome
        self.__dificuldade = dificuldade

        # Define limites com base na dificuldade
        if dificuldade == "facil":
            self.__limite = 15
        elif dificuldade == "medio":
            self.__limite = 10
        else:
            self.__limite = 5

        self.__numero_secreto = random.randint(1, 100)
        self.__tentativas = 0
        self.__pontuacao = 100  # começa com 100 pontos

    # ===============================
    # INICIAR JOGO
    # ===============================
    def iniciar(self):
        print("\n🎮 JOGO DA ADIVINHAÇÃO")
        print(f"Jogador: {self.__nome}")
        print(f"Dificuldade: {self.__dificuldade}")
        print("Adivinhe um número entre 1 e 100")
        print(f"Você tem {self.__limite} tentativas\n")

    # ===============================
    # LÓGICA DO JOGO
    # ===============================
    def jogar(self):
        while self.__tentativas < self.__limite:

            try:
                palpite = int(input("Digite seu palpite: "))
            except ValueError:
                print("⚠️ Digite um número válido!")
                continue

            self.__tentativas += 1

            # perde pontos a cada tentativa
            self.__pontuacao -= 10

            if palpite == self.__numero_secreto:
                print("🎉 Parabéns! Você acertou!")
                print(f"Pontuação: {self.__pontuacao}")
                return self.__pontuacao

            elif palpite < self.__numero_secreto:
                print("⬆️ O número secreto é MAIOR")

            else:
                print("⬇️ O número secreto é MENOR")

        print("\n❌ Você perdeu!")
        print("Número era:", self.__numero_secreto)
        return 0


# ===============================
# RANKING (LISTA DE JOGADORES)
# ===============================
ranking = []


def salvar_ranking(nome, pontuacao):
    ranking.append({"nome": nome, "pontuacao": pontuacao})


def exibir_ranking():
    print("\n🏆 RANKING")

    # Ordena do maior para o menor
    ranking_ordenado = sorted(ranking, key=lambda x: x["pontuacao"], reverse=True)

    for i, jogador in enumerate(ranking_ordenado, start=1):
        print(f"{i}º - {jogador['nome']} : {jogador['pontuacao']} pontos")


# ===============================
# FUNÇÃO PRINCIPAL
# ===============================
def executar_jogo():

    # Nome do jogador
    nome = input("Digite seu nome: ")

    # Escolha da dificuldade
    print("\nEscolha a dificuldade:")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")

    opcao = input("Opção: ")

    if opcao == "1":
        dificuldade = "facil"
    elif opcao == "2":
        dificuldade = "medio"
    else:
        dificuldade = "dificil"

    # Cria o jogo
    jogo = JogoAdivinhacao(nome, dificuldade)

    jogo.iniciar()
    pontuacao = jogo.jogar()

    # Salva no ranking
    salvar_ranking(nome, pontuacao)

    # Exibe ranking
    exibir_ranking()


# ===============================
# EXECUÇÃO
# ===============================
if __name__ == "__main__":
    while True:
        executar_jogo()

        continuar = input("\nQuer jogar novamente? (s/n): ").lower()
        if continuar != "s":
            break