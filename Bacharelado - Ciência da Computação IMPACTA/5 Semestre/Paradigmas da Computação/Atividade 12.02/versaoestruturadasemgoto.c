#include <stdio.h>

int main() {
    int nota;

    do {
        printf("Digite uma nota (0 a 10): ");
        scanf("%d", &nota);

        if (nota < 0 || nota > 10) {
            printf("Erro! Nota invalida.\n");
        }

    } while (nota < 0 || nota > 10);

    printf("Nota valida: %d\n", nota);
    return 0;
}
// O uso de estruturas como while e if torna o código mais claro e organizado, facilitando a leitura e a manutenção, mesmo em programas maiores e mais complexos.

