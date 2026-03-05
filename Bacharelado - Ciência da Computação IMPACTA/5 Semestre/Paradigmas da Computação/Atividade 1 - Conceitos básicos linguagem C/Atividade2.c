#include <stdio.h>
/*
- Qual a diferença entre *p e p?
	p é o endereço de memória armazenado, 
*p é o valor armazenado naquele endereço.

*/

int main() {
    int valor = 50;
    int *p = &valor; // 'p' guarda o endereço de 'valor'

    printf("Endereco (p): %p\n", p);   // Saída: 0x... (ex: 0x7ffd...)
    printf("Valor (*p): %d\n", *p);    // Saída: 50 (o valor armazenado em 'valor')
    
    *p = 100; // Modifica o valor no endereço p
    printf("Novo Valor (*p): %d\n", valor); // Saída: 100
    return 0;

}
/*
- Quando usar struct?
	É usado struct quando precisamos agrupar diferentes tipos de dados relacionados a uma única entidade em um único bloco de memório. 
Ex.: Cadastro de aluno, ponto 3D, produto.

- Quando usar passagem por referência?
	É usado passagem por referência principalmente para modificar variáveis originais fora do escopo da função, evitar cópias pesadas de estruturas/arrays grandes (aumentando eficiência) e retornar múltiplos valores de uma função.
- Crie uma struct chamada Produto com: nome, preço, quantidade
*/
struct Produto {
    char nome[50];
    float preco;
    int quantidade;
};

/*
- Criar função que receba o produto por referência e aumente o preço em 10%
*/

void aumentarPreco(struct Produto *produto) {
    produto->preco *= 1.1;
}