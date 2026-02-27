#include <stdio.h>

int main() {

    // 1. Definição do estado (variáveis)
    int numeros[] = {10, 20, 30, 40, 50};
    int soma = 0;
    int i;
    int tamanho = 5;

    // 2. Comandos imperativos (passo a passo)
    for (i = 0; i < tamanho; i++) {
        soma += numeros[i]; // Modifica o estado da variável 'soma'
    }

    // 3. Resultado
    printf("A soma é: %d\n", soma);

    return 0;
}