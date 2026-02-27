#include <stdio.h>

/* 
    Este programa demonstra o uso de ponteiros em C. Ele declara uma variável inteira 'x' e um ponteiro 'p' que aponta para 'x'. O programa imprime o valor de 'x', o endereço de memória de 'x' e o valor apontado por 'p', que é o mesmo que o valor de 'x'. O operador '*' é usado para acessar o valor apontado por 'p', enquanto '&' é usado para obter o endereço de memória de 'x'.
*/
int main() {
    int x = 25;
    int *p = &x;
    // O operador '&' é usado para obter o endereço de memória da variável 'x', e esse endereço é atribuído ao ponteiro 'p'. Assim, 'p' agora aponta para a variável 'x', permitindo que acessemos e modifiquemos o valor de 'x' através do ponteiro 'p' usando o operador '*'.
    printf("Valor de x: %d\n", x);
    printf("Endereco de x: %p\n", &x);
    printf("Valor apontado por p: %d\n", *p);

    return 0;
}