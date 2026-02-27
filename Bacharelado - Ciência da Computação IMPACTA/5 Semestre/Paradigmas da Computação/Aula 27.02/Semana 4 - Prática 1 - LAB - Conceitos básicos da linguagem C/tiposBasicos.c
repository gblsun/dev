#include <stdio.h>
// Este programa demonstra o uso de tipos básicos em C, como int, float e char, e como ler e imprimir esses valores usando scanf e printf.
// #include = diretiva de pré-processamento que inclui a biblioteca padrão de entrada e saída, permitindo o uso de funções como printf e scanf.
// <stdio.h> = biblioteca padrão de entrada e saída em C, que contém declarações para funções de entrada e saída, como printf e scanf.

/* 
    Este programa solicita ao usuário que insira sua idade, altura e a inicial do seu nome, e depois imprime um resumo dessas informações. Ele utiliza os tipos de dados básicos int para idade, float para altura e char para a inicial do nome, demonstrando como ler e imprimir esses tipos usando as funções de entrada e saída em C.
*/

int main() {
    int idade; 
    float altura;
    char inicial;

    printf("Digite sua idade: ");
    scanf("%d", &idade);
    // O '&' é necessário para passar o endereço da variável 'idade' para a função scanf, permitindo que ela armazene o valor digitado pelo usuário na variável correta.
    // Ou seja: %d = inteiro, &idade = endereço da variável idade.

    printf("Digite sua altura: ");
    scanf("%f", &altura);
    // O '&' é necessário para passar o endereço da variável 'altura' para a função scanf, permitindo que ela armazene o valor digitado pelo usuário na variável correta. 
    // Ou seja: %f = float, &altura = endereço da variável altura.

    printf("Digite a inicial do seu nome: ");
    scanf(" %c", &inicial); 
    // O '&' é necessário para passar o endereço da variável 'inicial' para a função scanf, permitindo que ela armazene o valor digitado pelo usuário na variável correta.
    // Ou seja: %c = caractere, &inicial = endereço da variável inicial. O espaço antes de %c é para ignorar qualquer caractere de nova linha que possa estar no buffer de entrada.

    printf("\nResumo:\n");
    printf("Idade: %d\n", idade);
    printf("Altura: %.2f\n", altura);
    printf("Inicial do nome: %c\n", inicial);
    // Aqui, usamos %d para imprimir a idade (inteiro), %.2f para imprimir a altura (float com 2 casas decimais) e %c para imprimir a inicial do nome (caractere).

    return 0;
    // A função main retorna 0 para indicar que o programa terminou com sucesso.
}