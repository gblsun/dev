#include <stdio.h>

int quadrado(int num) {
    // Esta função recebe um número inteiro como parâmetro e retorna o quadrado desse número. O cálculo é feito multiplicando o número por ele mesmo (num * num). O tipo de retorno da função é int, indicando que o resultado será um número inteiro.
    return num * num;
}

int main() {
    int valor;
    printf("Digite um numero: ");
    scanf("%d", &valor);

    printf("Quadrado de %d\n", quadrado(valor));
    return 0;
}