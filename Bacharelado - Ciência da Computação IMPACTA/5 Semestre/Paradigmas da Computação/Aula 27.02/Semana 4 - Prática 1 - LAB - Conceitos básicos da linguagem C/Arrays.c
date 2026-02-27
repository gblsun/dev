#include <stdio.h>

/* 
    Este programa demonstra o uso de arrays em C, permitindo que o usuário insira 5 números inteiros, armazene-os em um array e calcule a soma desses números. O programa utiliza um loop 'for' para iterar sobre os elementos do array, ler os valores inseridos pelo usuário e acumular a soma. Por fim, o resultado da soma é impresso na tela.
*/

int main(){
    int numeros[5];
    // Declaração de um array de inteiros chamado 'numeros' com capacidade para armazenar 5 elementos. O tipo 'int' indica que cada elemento do array será um número inteiro. O nome do array é 'numeros' e os colchetes '[]' indicam que se trata de um array, ou seja, uma estrutura de dados que pode armazenar múltiplos valores do mesmo tipo.
    int soma = 0;
    // Declaração de uma variável inteira chamada 'soma' e inicialização com o valor 0. Esta variável será usada para acumular a soma dos elementos do array 'numeros'. O tipo 'int' indica que 'soma' é um número inteiro, e a atribuição '= 0' define seu valor inicial como zero, garantindo que a soma comece do valor correto antes de adicionar os elementos do array.

    for(int i = 0; i < 5; i++) {
        // Início de um loop 'for' que itera 5 vezes, com a variável de controle 'i' começando em 0 e incrementando até 4. O loop é usado para percorrer os índices do array 'numeros', permitindo que o usuário insira um número em cada posição do array e acumule a soma desses números na variável 'soma'.
        printf("Digite um numero: ");
        scanf("%d", &numeros[i]);
        soma += numeros[i];
    }

    printf("A soma dos numeros é: %d\n", soma);
    
    return 0;
}