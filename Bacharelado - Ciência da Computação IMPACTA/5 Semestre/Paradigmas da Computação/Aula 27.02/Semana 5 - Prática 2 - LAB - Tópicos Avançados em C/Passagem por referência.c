#include <stdio.h>

/* 
    Este programa demonstra a passagem de parâmetros por referência em C.
    Ele define a função 'altera', que modifica o valor de um inteiro
    passado como argumento usando um ponteiro. Como a função recebe um
    ponteiro para a variável original, a alteração realizada dentro da
    função afeta diretamente a variável no 'main'. Assim, o valor impresso
    será 50, refletindo a modificação feita pela função 'altera'.
*/

void altera(int *x) {
    // Esta função recebe um ponteiro para um inteiro 'x' como parâmetro e atribui a ele o valor 50. O operador '*' é usado para acessar o valor apontado por 'x', permitindo que a função modifique diretamente a variável original passada pelo 'main'. Dessa forma, quando 'altera' é chamada com o endereço de 'numero', a alteração feita em '*x' dentro da função reflete na variável 'numero' do 'main', resultando na impressão do valor 50.
    *x = 50;
    // O operador '*' é usado para acessar o valor apontado por 'x', permitindo que a função modifique diretamente a variável original passada pelo 'main'. Assim, ao atribuir 50 a '*x', estamos alterando o valor da variável 'numero' que foi passada por referência, e não apenas uma cópia local dentro da função.
}

int main() {
    int numero = 10;
    altera(&numero);
    printf("Numero: %d\n", numero);
    return 0;
}