#include <stdio.h>
/* 
    Este programa demonstra o uso de endereços de memória em C. Ele declara uma variável inteira 'x', atribui um valor a ela e imprime tanto o valor quanto o endereço de memória onde 'x' está armazenada. O programa utiliza o especificador de formato '%d' para imprimir o valor inteiro e '%p' para imprimir o endereço de memória em formato hexadecimal.
*/

int main(){
    int x = 10;

    printf("Valor: %d\n", x);
    // O '%d' é um especificador de formato usado para imprimir um valor inteiro. Ele indica que o valor a ser impresso é do tipo int. O 'x' é a variável que contém o valor inteiro que queremos imprimir. Portanto, 'printf("Valor: %d\n", x);' irá imprimir a mensagem "Valor: 10" no console, onde '10' é o valor armazenado na variável 'x'.
    printf("Endereco: %p\n", &x);
    // O '%p' é um especificador de formato usado para imprimir um ponteiro, ou seja, um endereço de memória. O '&x' é o operador de endereço que retorna o endereço de memória onde a variável 'x' está armazenada. Portanto, 'printf("Endereco: %p\n", &x);' irá imprimir a mensagem "Endereco: 0x..." no console, onde '0x...' representa o endereço de memória hexadecimal onde a variável 'x' está localizada.

    return 0;
}