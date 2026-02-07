"""1. Crie uma classe chamada Aluno com:
Atributos:
nome,
notas (lista de floats).

Métodos:
adicionar_nota(valor) → adiciona uma nota à lista.
media() → retorna a média das notas.
situacao() → retorna "Aprovado" se média ≥ 7, senão "Reprovado".

2. Crie um objeto aluno com nome "Maria".
○ Adicione as notas: 8.0, 6.5, 7.5.
○ Mostre a média e a situação final."""


class Aluno:
    def __init__(self, nome, notas=None):
        self.nome = nome
        self.notas = [float(nota) for nota in notas] if notas else []

    def adicionar_nota(self, valor):
        self.notas.append(float(valor))

    def media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        return "Aprovado" if self.media() >= 7 else "Reprovado"


# ---- Testando o programa ----
aluno_maria = Aluno("Maria")

# Adicionando notas
aluno_maria.adicionar_nota(8.0)
aluno_maria.adicionar_nota(6.5)
aluno_maria.adicionar_nota(7.5)

# Mostrando média e situação final
print(f"Média: {aluno_maria.media():.2f}")
print(f"Situação: {aluno_maria.situacao()}")
