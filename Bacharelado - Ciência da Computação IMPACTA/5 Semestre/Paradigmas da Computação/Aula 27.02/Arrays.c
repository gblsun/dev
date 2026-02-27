#include <stdio.h>

int main(){
    int numeros[5];
    int soma = 0;

    for(int i = 0; i < 5; i++) {
        printf("Digite um numero: ");
        scanf("%d", &numeros[i]);
        soma += numeros[i];
    }

    printf("A soma dos numeros é: %d\n", soma);
    
    return 0;
}