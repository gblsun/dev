# %%
# imports
# TODO: inclua aqui os imports (se necessário)


# funções
"""
O objetivo da função é retornar a lista de disciplinas ministradas pelo(a) professor(a) que recebeu como parâmetro.

se a lista de professores estiver vazia 
    a função retorna uma lista vazia. 
Quando há ao menos um(a) professor(a) na lista 
    a função verifica se o nome do(a) primeiro(a) professor(a) corresponde ao nome pesquisado. 
Caso tal verificação resulte em positivo, 
    a função retorna os nomes das disciplinas desse(a) professor(a). 
Se o nome não é encontrado no primeiro(a) professor(a), a função se chama recursivamente com o restante da lista de professores, passando o mesmo nome do(a) professor(a) para continuar a busca.


"""

# corrigir!!!!!
def listar_disciplinas(professores, nome_professor):
    lista_vazia = set()
    if len(professores) == 0:
        return lista_vazia
    else:
        if 
        professores["nome"] == nome_professor:
            print(professores["disciplinas['nome_disciplina']"])
        else:
            return professores.pop[0] 


# programa principal
professores = [
    {
        "matricula": 1001,
        "nome": "João Silva",
        "cargo": "Professor Adjunto",
        "email": "joao.silva@faculdadeimpacta.com.br",
        "disciplinas": [
            {
                "codigo": "APA301",
                "nome_disciplina": "Análise e Projeto de Algoritmos",
                "turma": "CC3AM",
                "quantidade_alunos": 30,
            },
            {
                "codigo": "AED302",
                "nome_disciplina": "Algoritmos e Estruturas de Dados",
                "turma": "CC3AM",
                "quantidade_alunos": 25,
            },
        ],
    },
    {
        "matricula": 1002,
        "nome": "Maria Oliveira",
        "cargo": "Professora Associada",
        "email": "maria.oliveira@faculdadeimpacta.com.br",
        "disciplinas": [
            {
                "codigo": "LOO401",
                "nome_disciplina": "Linguagem Orientada a Objetos",
                "turma": "CC4AN",
                "quantidade_alunos": 40,
            },
            {
                "codigo": "TC402",
                "nome_disciplina": "Teoria da Computação",
                "turma": "CC4AM",
                "quantidade_alunos": 35,
            },
        ],
    },
    {
        "matricula": 1003,
        "nome": "Carlos Pereira",
        "cargo": "Professor Titular",
        "email": "carlos.pereira@faculdadeimpacta.com.br",
        "disciplinas": [
            {
                "codigo": "DBD701",
                "nome_disciplina": "Desenvolvimento para Big Data",
                "turma": "CC7AN",
                "quantidade_alunos": 28,
            },
            {
                "codigo": "COMP601",
                "nome_disciplina": "Compiladores",
                "turma": "CC6AM",
                "quantidade_alunos": 22,
            },
        ],
    },
    {
        "matricula": 1004,
        "nome": "Ana Costa",
        "cargo": "Professora Adjunta",
        "email": "ana.costa@faculdadeimpacta.com.br",
        "disciplinas": [
            {
                "codigo": "TG503",
                "nome_disciplina": "Teoria de Grafos",
                "turma": "CC5AM",
                "quantidade_alunos": 33,
            },
            {
                "codigo": "PIVC801",
                "nome_disciplina": "Processo de Imagens e Visão Computacional",
                "turma": "CC8AM",
                "quantidade_alunos": 27,
            },
        ],
    },
]

print(
    listar_disciplinas(professores, "João Silva")
)  # ['Análise e Projeto de Algoritmos', 'Algoritmos e Estruturas de Dados']
print(listar_disciplinas(professores, "Vitor Furlan"))  # professor(a) não encontrado(a)

# %%
