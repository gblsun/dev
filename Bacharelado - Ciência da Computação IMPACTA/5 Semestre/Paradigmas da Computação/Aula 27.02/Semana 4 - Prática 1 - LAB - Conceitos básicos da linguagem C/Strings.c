#include <stdio.h>
#include <string.h>
// string.h é uma biblioteca padrão em C que contém funções para manipulação de strings, como strlen, strcpy, strcat, entre outras. Neste programa, utilizaremos a função strlen para calcular o comprimento da string inserida pelo usuário.

/* 
    Este programa solicita ao usuário que insira seu nome, armazena o nome em um array de caracteres (string) e depois imprime o nome e a quantidade de letras que ele contém. O programa utiliza a função scanf para ler a entrada do usuário e a função strlen para calcular o comprimento da string, ou seja, o número de caracteres presentes no nome.
*/

int main() {
    char nome[50];
    // Declaração de um array de caracteres chamado 'nome' com capacidade para armazenar até 50 caracteres. O tipo 'char' indica que cada elemento do array é um caractere, e os colchetes '[]' indicam que se trata de um array. O número 50 especifica o tamanho máximo do array, ou seja, a quantidade máxima de caracteres que podem ser armazenados, incluindo o caractere nulo '\0' que indica o final da string.

    printf("Digite seu nome: ");
    scanf("%s", nome);

    printf("Nome: %s\n", nome);
    printf("Quantidade de letras: %lu\n", strlen(nome));
    // A função strlen é usada para calcular o comprimento da string armazenada na variável 'nome'. Ela retorna o número de caracteres presentes na string, excluindo o caractere nulo '\0' que indica o final da string. O especificador de formato '%lu' é usado para imprimir o valor retornado por strlen, que é do tipo size_t (um tipo inteiro sem sinal). Portanto, 'printf("Quantidade de letras: %lu\n", strlen(nome));' irá imprimir a mensagem "Quantidade de letras: X" no console, onde 'X' é o número de caracteres no nome inserido pelo usuário.

    return 0;
}

/*
    A função `scanf` com o especificador `%s` lê apenas uma sequência contínua de caracteres até encontrar um espaço em branco, como espaço, tabulação ou quebra de linha, o que faz com que apenas a primeira palavra de um nome composto seja armazenada. 
    Já a função `fgets` lê toda a linha de entrada até o limite do buffer ou até encontrar uma quebra de linha, permitindo capturar nomes completos com espaços de forma mais segura e previsível; por isso, `fgets` é geralmente a escolha mais adequada quando se deseja ler textos inteiros, enquanto `scanf("%s", ...)` é mais indicado apenas para palavras isoladas.
*/