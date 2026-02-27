#include <stdio.h>

struct aluno {
    char nome[50];
    int idade;
    float nota;
};

int main() {
    struct aluno a1;

    printf("Digite o nome do aluno: ");
    scanf("%s", a1.nome);  
    // O scanf("%s") lê somente até o primeiro espaço.
    // Portanto, funciona para "Gabriel", mas não para "Gabriel Silva".

    /* 
        ALTERNATIVA (NÃO IMPLEMENTADA):
        fgets(a1.nome, 50, stdin);
        Motivo da mudança:
        - fgets permite ler nomes completos com espaços, pois lê a linha inteira.
        - Evita o problema do scanf parar no espaço.
    */

    printf("Digite a idade do aluno: ");
    scanf("%d", &a1.idade);

    printf("Digite a nota do aluno: ");
    scanf("%f", &a1.nota);

    printf("Aluno: %s\n", a1.nome);
    printf("Idade: %d\n", a1.idade);
    printf("Nota: %.2f\n", a1.nota);

    return 0;
}