# Aula 7: técnicas de programação IMPACTA 30 de Agosto de 2024
# Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)

# Recursividade Memoização


'''
    Sabendo que 10! = 3.628.800, como você faria para calcular 11! ?

Uma possível solução é calcular: 11*10*9*8*7*6*5*4*3*2*1

Uma solução mais eficiente é calcular: 11*10! = 11* 3.628.800

Porém, só foi possível calcular 11! utilizando o resultado de 10! porque, anteriormente, játínhamos calculado 10! e, acima de tudo, porque lembrávamos do resultado
'''


# %% Exemplo: Fatorial
def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n-1)
    
'''
Quando queremos calcular 10! com a função fatorial, é necessário que ela também calcule o fatorial de todos os números inteiros menores que 10

Se, em um momento posterior, queremos calcular 11!, todos os cálculos anteriores teriam que ser refeitos!

Sabemos também que a função fatorial sempre produz o mesmo resultado para um dado valor passado como parâmetro

Será que podemos pensar em armazenar alguns resultados da função fatorial para que possam ser reutilizados?'''

# %% Exemplo fatorial recursivo 
'''Ideia: criar um dicionário para armazenar resultados previamente calculados para a função'''
CACHE = {}

def fatorial(valor):
    if valor in CACHE:
        return CACHE[valor]
    else:
        if valor <= 1:
            CACHE[valor] = 1
            return CACHE[valor]
        else:
            CACHE[valor] = valor * fatorial (valor - 1)
            return CACHE[valor]
        
print(fatorial(5))
print(fatorial(6))

'''
Python thuthor:
https://pythontutor.com/python-compiler.html#mode=edit

Cacheamento de valores

A ideia de cacheamento (caching) consiste em armazenar dados que o programa utilize com frequência no código. Dessa forma, esse dados não serão gerados múltiplas vezes, pois estarão previamente salvos

O cache é amplamente utilizado em diversos sistemas e aplicações para melhorar o desempenho e reduzir o tempo de acesso a dados frequentemente solicitados. Exemplos:

    Cache de Navegadores Web;
    Cache de DNS;
    Cache de Processadores;
    Cache de Banco de Dados;
    Cache de Video Streaming.


Memoização 

Memoização consiste em armazenar resultados de funções cujo custo computacional é alto, visando retornar o mesmo resultado, caso os mesmo parâmetros sejam passados na respectiva função

Funcionam para qualquer tipo de função?

Exemplo 1: função fatorial(n), que retorna o fatorial de um número natural n. 
    Valhe a pena e faz sentido utilizar da memoização na função fatorial.

Exemplo 2: função que_horas_sao(), que retorna o horário atual.
    Não valhe a pena utilizar da memoização e cache e acaba nos atrapalhando do que ajudando.

Funções puras e impuras

Função pura: dado um conjunto de valores para os parâmetros, o resultado produzido será sempre o mesmo. É determinística.
    Só pode utilizar memoização na função pura!

Função impura: pode não produzir o mesmo resultado para as mesmas entradas. Não determinísticas.
    Na função impura não pode utilizar memoização
    
<------importante------>
Memoização com functools

O functools é um módulo que fornece funções de ordem superior. Ele é especialmente útil para manipular funções de forma mais avançada.

O decorador functools.cache é usado para criar um cache de resultados de uma função. Cada vez que a função é chamada com o mesmo argumento, ela não é executada novamente; em vez disso, o resultado já computado no cache é retornado.
'''
# %% Memoização com functools
# Utilizando decorador lru_cache
from functools import lru_cache

@lru_cache
def fatorial_com_cache(valor):
    if valor <= 1:
        return 1
    else:
        return valor * fatorial_com_cache(valor - 1)
    
def fatorial_sem_cache(valor):
    if valor <= 1:
        return 1
    else:
        return valor * fatorial_sem_cache(valor - 1)

# %% --end
