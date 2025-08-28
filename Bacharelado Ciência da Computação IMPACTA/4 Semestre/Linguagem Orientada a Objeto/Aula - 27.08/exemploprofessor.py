# Definindo a classe
class Pessoa:
    """
    class → Palavra reservada do Python usada para criar classes.
    Classe é como um molde (ou "fôrma") que define as características (atributos) e comportamentos (métodos) de um objeto.
    Aqui criamos a classe Pessoa, que representa uma pessoa.
    """
    def __init__(self, nome, idade):
        """
        def → define uma função ou método.
        __init__ → é um método especial, chamado automaticamente quando criamos uma nova pessoa. Ele é conhecido como construtor.
        
        self → referência ao próprio objeto que está sendo criado.
        (É como dizer: “essa variável nome pertence a essa pessoa específica.”)
        nome e idade → informações que vamos passar na hora de criar a pessoa.
        """
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade}")

    def fazer_aniversario(self):
        self.idade += 1
        print(f"Parabéns {self.nome}! Agora você tem {self.idade} anos.")


# Criando objetos (instâncias)
p1 = Pessoa("Ana", 25)
p2 = Pessoa("Carlos", 30)

# Chamando os métodos
p1.apresentar()
p1.fazer_aniversario()
p1.apresentar()

print("---")

p2.apresentar()
p2.fazer_aniversario()
p2.apresentar()
