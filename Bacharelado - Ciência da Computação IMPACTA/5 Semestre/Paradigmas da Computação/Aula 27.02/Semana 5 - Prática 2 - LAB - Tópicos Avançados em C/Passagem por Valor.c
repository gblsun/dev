#include <stdio.h>

/* 
    Este programa demonstra a passagem de parâmetros por valor em C.
    Ele define a função 'altera', que tenta modificar o valor de um inteiro
    passado como argumento. Entretanto, como a linguagem C utiliza passagem
    por valor, a alteração realizada dentro da função não afeta a variável
    original no 'main'. Assim, o valor impresso permanece 10, e não 50.
*/

void altera(int x){
    /*
        Esta função recebe um número inteiro 'x' como parâmetro e tenta
        atribuir a ele o valor 50. No entanto, como a passagem de parâmetros
        em C é feita por valor, 'x' é apenas uma cópia da variável 'numero'
        declarada no 'main'. Dessa forma, qualquer alteração feita em 'x'
        dentro da função não modifica o valor original de 'numero'.

        O tipo 'void' indica que a função não retorna nenhum valor, e
        'int x' representa um parâmetro de entrada que recebe uma cópia
        do valor passado pelo 'main'.
    */
    x = 50;
}

int main() {
    int numero = 10;
    altera(numero);
    printf("Numero: %d\n", numero);
    return 0;
}