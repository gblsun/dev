#include <stdio.h>

int main() {
    int nota;
inicio:
    printf("Digite uma nota (0 a 10): ");
    scanf("%d", &nota);
    if (nota < 0 || nota > 10)
        goto erro;
    printf("Nota valida: %d\n", nota);
    goto fim;
erro:
    printf("Erro! Nota invalida.\n");
    goto inicio;
fim:
    return 0;
}
A